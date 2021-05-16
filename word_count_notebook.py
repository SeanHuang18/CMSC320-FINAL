import io
import json

with io.open('salareis_test.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

word_count = 0
for cell in nb:
    if cell.cell_type == "markdown":
        word_count += len(cell['source'].replace('#', '').lstrip().split(' '))
print(word_count)