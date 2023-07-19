import pandas as pd

# List of your CSV files
csv_files = ['transcripts_0.csv', 'transcripts_1.csv', 'transcripts_2.csv']

for file in csv_files:
    # Load the CSV file
    df = pd.read_csv(file, delimiter='^')

    # Get the first and last transcript
    first_transcript = df.iloc[0]
    last_transcript = df.iloc[-1]

    # Print out the id and episode_id values
    print(f'File: {file}')
    print('First transcript:')
    print('id:', first_transcript['id'])
    print('episode_id:', first_transcript['episode_id'])
    print('Last transcript:')
    print('id:', last_transcript['id'])
    print('episode_id:', last_transcript['episode_id'])
    print('---')
