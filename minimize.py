import re
import os
from collections import OrderedDict

dev_re = re.compile(
    "\/\/\s*?\%start_dev\%.+?\/\/\s*?\%end_dev\%", flags=re.MULTILINE | re.DOTALL
)
multiline_comment_re = re.compile(
    "/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/", flags=re.MULTILINE
)
comment_re = re.compile("//.*")
ops_re = re.compile(
    r" *(\||\/|\+|\-|\=|\&|\<|\>|\,|\!|\:(?!$)) *(?!(@|`|\?))", flags=re.MULTILINE
)
trace_re = re.compile(r"trace\(.+?\)", flags=re.MULTILINE)
foe_re = re.compile(r"\bfoe\b(?!\.)")
loc_re = re.compile(r"\bloc\b(?!\.)")

sep = """
/*********************
**     #Progress    **
*********************/"""


replacements = OrderedDict((
    ("foe.armor", "fa"),
    ("foe.count", "fc"),
    ("foe.distance", "fd"),
    ("foe.hp", "fh"),
    ("foe.id", "fi"),
    ("foe.maxhp", "fm"),
    ("foe.state", "fs"),
    ("foe.time", "ft"),
    ("totaltime", "tt"),
))
def minimize_safe(text):
    text = multiline_comment_re.sub("", text)
    text = comment_re.sub("", text)
    text = ops_re.sub("\g<1>", text)
    text = foe_re.sub("ff", text)
    text = loc_re.sub("ll", text)
    text = (text
    .replace("found", "f")
    .replace("can_activate", "ca")
    .replace("can_use", "cu")
    .replace("try_equip", "te")
    .replace("auto_equip", "ae")
    .replace("find_", "f_")
    .replace("is_boss", "ib")
    .replace("can_be_debuffed", "cbd")
    .replace("disable_r", "dr")
    )
    vars_1 = ['var ff=foe', 'var ll=loc']
    vars_2 = ['  ff=foe', '  ll=loc']
    ff = False
    ll = False
    for src, dst in replacements.items():
        text = text.replace(src, dst)
        vars_1.append(f'var {dst}=0')
        vars_2.append(f'  {dst}={src}')
    text = text.replace(
        "func _update_game_state()\n",
        '{}\nfunc _update_game_state()\n{}\n'.format('\n'.join(vars_1), '\n'.join(vars_2))
    )
    return text


def process_release(header, body):
    header = header.replace("var ui_show_debug = true", "var ui_show_debug = false")
    header = header.replace("var enable_tracing = true\n", "")
    header = header.replace("var enable_tracing = false\n", "")
    header = header.replace("var enable_hit_tracking = true\n", "")
    header = header.replace("var enable_hit_tracking = false\n", "")
    body = body.replace("traces.Clear()", "")
    body = body.replace("  enable_hit_tracking = false", "")
    body = dev_re.sub("", body)
    body = trace_re.sub("", body)
    body = minimize_safe(body)
    new_body = []
    new_header = []
    for line in body.splitlines():
        line = line.rstrip()
        if line:
            new_body.append(line)
    for line in header.splitlines():
        line = line.rstrip()
        new_header.append(line)
    return new_header, new_body


def process_debug(header, body):
    header = header.replace("var enable_tracing = false", "var enable_tracing = true")
    header = header.replace("var ui_show_debug = false", "var ui_show_debug = true")
    header = header.replace(
        "var enable_hit_tracking = true", "var enable_hit_tracking = false"
    )
    body = minimize_safe(body)
    new_body = []
    new_header = []
    for line in body.splitlines():
        line = line.rstrip()
        if line:
            new_body.append(line)
    for line in header.splitlines():
        line = line.rstrip()
        if line:
            new_header.append(line)
    return new_header, new_body


def minimize():
    with open("scribble.dev.txt", mode="r", encoding="utf-8") as f:
        whole = f.read()
    parts = whole.split(sep)
    release_header, release_body = process_release(parts[0], parts[1])
    debug_header, debug_body = process_debug(minimize_safe(parts[0]), parts[1])
    with open("scribble.txt", mode="w", encoding="utf-8") as f:
        f.write("\n".join(release_header) + "\n\n" + "\n".join(release_body))
    with open("scribble.debug.txt", mode="w", encoding="utf-8") as f:
        f.write("\n".join(debug_header) + "\n" + "\n".join(debug_body))
    for fname in ("scribble.dev.txt", "scribble.txt", "scribble.debug.txt"):
        size = os.stat(fname).st_size / 1024
        print(f"{fname.rjust(len('scribble.debug.txt'))}: {size} kb")
        if not "dev" in fname and size > 40:
            print(f"WARNING: {fname} is over 40kb!")


if __name__ == "__main__":
    minimize()
