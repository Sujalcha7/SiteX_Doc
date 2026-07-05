import os
import re

tex_files = []
base_dir = r"d:\projects\Finalproject\SiteX_Doc"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.tex'):
            tex_files.append(os.path.join(root, file))

abbreviations = set()
pattern = re.compile(r'\b[A-Z]{2,}\b')

for f in tex_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = pattern.findall(content)
            abbreviations.update(matches)
    except Exception as e:
        print(f"Error reading {f}: {e}")

sorted_abbr = sorted(list(abbreviations))

with open(r"d:\projects\Finalproject\SiteX_Doc\abbr_utf8.txt", 'w', encoding='utf-8') as out:
    out.write("\n".join(sorted_abbr))
print("Done")
