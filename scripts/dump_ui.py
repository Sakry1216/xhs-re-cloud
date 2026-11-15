import re
import sys

try:
    t = open(sys.argv[1], encoding="utf-8", errors="replace").read()
except Exception as e:
    print("parse err", e)
    sys.exit()
for m in re.finditer(r'text="([^"]{1,60})"', t):
    print("TEXT:", m.group(1))
