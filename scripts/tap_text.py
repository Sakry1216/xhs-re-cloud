import re
import sys

texts = sys.argv[2].split(",")
try:
    t = open(sys.argv[1], encoding="utf-8", errors="replace").read()
except Exception:
    print("")
    sys.exit()
for m in re.finditer(r'text="([^"]+)"[^>]*bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', t):
    if m.group(1).strip().lower() in [x.lower() for x in texts]:
        x = (int(m.group(2)) + int(m.group(4))) // 2
        y = (int(m.group(3)) + int(m.group(5))) // 2
        print(str(x) + " " + str(y))
        sys.exit()
print("")
