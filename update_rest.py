import re, glob

# Files to process
files = glob.glob('chapter/*.tex') + ['intro.tex']

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replacements
    text = re.sub(r'(?i)xgboost regressor', 'Heterogeneous Graph Attention Network (HeteroGAT)', text)
    text = re.sub(r'XGBoost Learning Curve', 'Learning Curve', text)
    text = re.sub(r'img/XGBoostLearningCurve.png', 'img/HeteroGATLearningCurve.png', text)
    text = re.sub(r'XGBoost algorithm', 'HeteroGAT architecture', text)
    text = re.sub(r'XGBoost ', 'HeteroGAT ', text)
    text = re.sub(r'XGBoost,', 'PyTorch Geometric,', text)
    text = re.sub(r'models such as XGBoost', 'models such as HeteroGAT', text)
    text = re.sub(r'the current XGBoost-based approach', 'the current graph-based approach', text)
    text = re.sub(r'While XGBoost provides', 'While simpler models provide', text)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

print('Done everywhere.')
