import pandas as pd
df = pd.read_csv('title.basics.tsv', sep='\t')
df = df.head(10000)
df.to_csv('title.basics.tsv', sep='\t', index=False)