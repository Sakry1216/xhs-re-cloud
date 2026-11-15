import re
import sys

cands = [x.strip() for x in sys.argv[2].split(",") if x.strip()]
try:
    t = open(sys.argv[1], encoding="utf-8", errors="replace").read()
except Exception:
    print("")
    sys.exit()
nodes = []
for m in re.finditer(r'text="([^"]+)"[^>]*bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', t):
    txt = m.group(1).strip()
    x = (int(m.group(2)) + int(m.group(4))) // 2
    y = (int(m.group(3)) + int(m.group(5))) // 2
    nodes.append((txt, x, y))
for c in cands:
    for txt, x, y in nodes:
        if txt.lower() == c.lower():
            print(f"{x} {y}")
            sys.exit()
    for txt, x, y in nodes:
        if c.lower() in txt.lower():
            print(f"{x} {y}")
            sys.exit()
print("")
