import pandas as pd

# List of your CSV files
csv_files = ['transcripts_0.csv', 'transcripts_1.csv', 'transcripts_2.csv']

for i, file in enumerate(csv_files):
    # Load the CSV file
    df = pd.read_csv(file, delimiter='^')

    # Subtract the minimum id and episode_id from all ids and episode_ids to make them start from 1
    df['id'] = df['id'] - df['id'].min() + 1 + i*1000
    df['episode_id'] = df['episode_id'] - df['episode_id'].min() + 1 + i*1000

    # Reorder the columns
    df = df[['id', 'podcast_id', 'episode_id', 'transcript']]

    # Save the DataFrame back to the CSV file
    df.to_csv(file, index=False, sep='^')
