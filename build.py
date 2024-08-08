import os
import subprocess


files = os.listdir(os.curdir)
for f in files:
    if f[-3:] == '.md' and f != "README.md":
        subprocess.run(["pandoc", f, "-s", "-o", f[:-3] + ".pdf", "--wrap=preserve"])
