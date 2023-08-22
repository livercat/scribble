import re
import os

multiline_comment_re = re.compile(
    "/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/", flags=re.MULTILINE
)
comment_re = re.compile("//.*")

sep = """
/*********************
**     #Progress    **
*********************/"""


def minimize():
    with open("dev.scribble.txt", mode="r", encoding="utf-8") as f:
        whole = f.read()
    parts = whole.split(sep)
    body = multiline_comment_re.sub("", parts[1])
    body = comment_re.sub("", body)
    new_body = []
    new_header = []
    new_min_header = []
    min_header = multiline_comment_re.sub("", parts[0])
    min_header = comment_re.sub("", min_header)
    for line in parts[0].splitlines():
        line = line.rstrip()
        new_header.append(line)
    for line in body.splitlines():
        line = line.rstrip()
        if line:
            new_body.append(line)
    for line in min_header.splitlines():
        line = line.rstrip()
        if line:
            new_min_header.append(line)
    with open("scribble.txt", mode="w", encoding="utf-8") as f:
        f.write("\n".join(new_header) + "\n\n" + "\n".join(new_body))
    with open("min.txt", mode="w", encoding="utf-8") as f:
        f.write("\n".join(new_min_header) + "\n" + "\n".join(new_body))
    for fname in ("dev.scribble.txt", "scribble.txt", "min.txt"):
        size = os.stat(fname).st_size / 1024
        print(f"{fname.rjust(len('dev.scribble.txt'))}: {size} kb")
        if not fname.startswith("dev") and size > 40:
            print(f"WARNING: {fname} is over 40kb!")


if __name__ == "__main__":
    minimize()
