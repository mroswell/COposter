from pathlib import Path

fm_tmpl = """\
---
title: "{title}"
date: 2022-6-7T11:02:05+06:00
lastmod: 2022-6-7T11:02:05+06:00
url: "{url}"
weight: 3
draft: false
# search related keywords
keywords: [""]
---
"""

root = Path('./static/markdown/').resolve()
folders = ['conditionsmd', 'risksmd']

for folder in folders:
    for file in (root / folder).glob('*.md'):
        title = file.stem.replace('-', ' ').title()
        url = f'{folder[:-2]}/{file.stem}'
        frontmatter = fm_tmpl.format(title=title, url=url)
        content = f"{frontmatter}\n{file.read_text()}"
        file.write_text(content)