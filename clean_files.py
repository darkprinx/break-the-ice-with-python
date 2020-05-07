import re
from pathlib import Path

p = Path('./copy/Status')

for file in p.iterdir():
    with open(file, 'r+') as f:
        content = f.read()
        new_content = re.sub(r'My Solution: Python 3', r'Solutions: ', content, flags=re.MULTILINE | re.DOTALL)
        with open(file.name, "w+") as r:
            r.write(new_content)