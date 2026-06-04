import os, glob

replacements = {
    'HeteroGAT': 'HeteroGNN',
    'Heterogeneous Graph Attention Network': 'Heterogeneous Graph Neural Network',
    'Graph Attention Network (GAT)': 'Graph Neural Network (GNN)',
    'Heterogeneous GAT': 'Heterogeneous GNN',
    'GAT layer': 'GNN layer'
}

files = glob.glob('**/*.tex', recursive=True) + glob.glob('README.md')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content
    for old_str, new_str in replacements.items():
        new_content = new_content.replace(old_str, new_str)
        
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
