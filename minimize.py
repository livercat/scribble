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
    with open("scribble.txt", mode="r", encoding="utf-8") as f:
        text = f.read()
    parts = text.split(sep)
    text = multiline_comment_re.sub("", parts[1])
    text = comment_re.sub("", text)
    new_text = []
    for line in parts[0].splitlines():
        line = line.rstrip()
        new_text.append(line)
    for line in text.splitlines():
        line = line.rstrip()
        if line:
            new_text.append(line)
    with open("release.txt", mode="w", encoding="utf-8") as f:
        f.write("\n".join(new_text))
    print(f"old: {os.stat('scribble.txt').st_size/1024} Kb")
    print(f"new: {os.stat('release.txt').st_size/1024} Kb")


if __name__ == "__main__":
    minimize()
