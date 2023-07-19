import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('episodes_transcripts.csv', delimiter='^')

# Split the data into 18 smaller dataframes
dfs = np.array_split(df, 21)  # Change the number to split into more files

# Save each smaller dataframe to a new CSV file
for i, df in enumerate(dfs):
    df.to_csv(f'episodes_transcripts_{i}.csv', index=False, sep='^')
