import pandas as pd

# List of your CSV files
csv_files = ['transcripts_0.csv', 'transcripts_1.csv', 'transcripts_2.csv']

# Initialize a counter for the id and episode_id
counter = 1

for file in csv_files:
    # Load the CSV file
    df = pd.read_csv(file, delimiter='^')

    # Get the number of rows in the DataFrame
    num_rows = len(df)

    # Create new id and episode_id values that start from the current value of counter
    df['id'] = range(counter, counter + num_rows)
    df['episode_id'] = range(counter, counter + num_rows)

    # Update the counter
    counter += num_rows

    # Reorder the columns
    df = df[['id', 'podcast_id', 'episode_id', 'transcript']]

    # Save the DataFrame back to the CSV file
    df.to_csv(file, index=False, sep='^')
