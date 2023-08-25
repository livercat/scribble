import re
import os

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

sep = """
/*********************
**     #Progress    **
*********************/"""


def minimize_safe(text):
    text = multiline_comment_re.sub("", text)
    text = comment_re.sub("", text)
    text = ops_re.sub("\g<1>", text)
    text = (
        text.replace("foe.state", "fs")
        .replace("foe.time", "ft")
        .replace("foe.distance", "fd")
        .replace("foe.id", "fi")
        .replace("foe.count", "fc")
    )
    text = text.replace(
        "func _update_game_state()\n",
        'var fs=0\nvar ft=0\nvar fd=0\nvar fc=0\nvar fi=""\n'
        "func _update_game_state()\n  fs=foe.state\n  ft=foe.time\n  "
        "fd=foe.distance\n  fc=foe.count\n  fi=foe.id\n",
    )
    return text


def process_release(header, body):
    header = header.replace("var ui_show_debug = true", "var ui_show_debug = false")
    header = header.replace("var enable_tracing = true\n", "")
    header = header.replace("var enable_tracing = false\n", "")
    header = header.replace("var enable_hit_tracking = true\n", "")
    header = header.replace("var enable_hit_tracking = false\n", "")
    body = body.replace("traces.Clear()", "")
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
