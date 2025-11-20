from pathlib import Path
import time

CURRENT_DIR = Path('./dir/').resolve()

for filepath in CURRENT_DIR.iterdir():
    time.sleep(1)
    with open(filepath) as f:
        print(f.read())