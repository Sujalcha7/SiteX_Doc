import re

file_path = 'chapter/chapter_5.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace all occurrences of XGBoost references in Chapter 5
text = re.sub(r'XGBoost model file', r'Heterogeneous Graph Attention Network (HeteroGAT) model file', text)
text = re.sub(r'XGBoost model', r'HeteroGAT model', text)
text = re.sub(r'trained Model \(XGBoost\)', r'Trained Model (HeteroGAT)', text)
text = re.sub(r'Trained XGBoost Model', r'Trained HeteroGAT Model', text)
text = re.sub(r'Primary Model \(XGBoost\)', r'Primary Model (HeteroGAT)', text)
text = re.sub(r'\\texttt\{xgb\.XGBRegressor\}, a gradient boosted decision tree algorithm', r'A Heterogeneous Graph Attention Network (HeteroGAT)', text)
text = re.sub(r'XGBoost Learning Curve', r'HeteroGAT Learning Curve', text)
text = re.sub(r'XGBoost Regression', r'Geometric Deep Learning', text)
text = re.sub(r'XGBoost regression', r'HeteroGAT deep learning', text)
text = re.sub(r'XGBoost regressor', r'HeteroGAT architecture', text)
text = re.sub(r'XGBoost Regressor', r'HeteroGAT model', text)
text = re.sub(r'xgb\_baseline\.pkl', r'heterogat\_v1.pt', text)
text = re.sub(r'xgboost-arch', r'heterogat-arch', text)
text = re.sub(r'in the XGBoost training notebook', r'in the geometric deep learning training notebook', text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Chapter 5 updated.')
