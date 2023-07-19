import pandas as pd

# List of your CSV files
csv_files = ['transcripts_0.csv', 'transcripts_1.csv', 'transcripts_2.csv']

for file in csv_files:
    # Load the CSV file
    df = pd.read_csv(file, delimiter='^')

    # Print out some basic information
    print(f'File: {file}')
    print('Number of rows:', len(df))
    print('Number of null values in each column:')
    print(df.isnull().sum())
    print('---')
