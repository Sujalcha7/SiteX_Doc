import re

file_path = 'chapter/chapter_5.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('XGBoost', 'HeteroGAT')
text = text.replace('xgboost', 'heterogat')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Done')
