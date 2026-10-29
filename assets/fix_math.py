r"""Make $...$ math safe for GitHub's MathJax renderer:
- inside math: < -> \lt, > -> \gt (unless already a LaTeX macro like \lt, \ll, <= etc.)
- inside math located in table rows: |x| -> \lvert x\rvert (bare | splits table cells)
Usage: python3 fix_math.py file.md [...]"""
import re
import sys

MATH = re.compile(r"(\$\$.*?\$\$|\$[^$\n]+?\$)", re.S)


def fix_segment(seg: str, in_table: bool) -> str:
    body = seg
    # angle brackets: replace bare < and > not preceded by backslash
    body = re.sub(r"(?<!\\)<(?!<)", r"\\lt ", body)
    body = re.sub(r"(?<!\\)>(?!>)", r"\\gt ", body)
    body = body.replace("\\lt =", "\\le ").replace("\\gt =", "\\ge ")
    if in_table:
        # pair bare pipes left-to-right as \lvert ... \rvert
        parts = re.split(r"(?<!\\)\|", body)
        if len(parts) > 1 and len(parts) % 2 == 1:
            out = parts[0]
            for i, p in enumerate(parts[1:], 1):
                out += ("\\lvert " if i % 2 == 1 else "\\rvert ") + p
            body = out
        else:
            body = re.sub(r"(?<!\\)\|", "\\\\vert ", body)
    return body


def fix_file(path: str) -> int:
    lines = open(path, encoding="utf-8").read().split("\n")
    changed = 0
    for i, line in enumerate(lines):
        in_table = line.lstrip().startswith("|")
        new = MATH.sub(lambda m: fix_segment(m.group(0), in_table), line)
        if new != line:
            lines[i] = new
            changed += 1
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return changed


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(f"{p}: {fix_file(p)} lines changed")
