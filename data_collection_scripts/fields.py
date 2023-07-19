import pandas as pd

# Load the data
df = pd.read_csv("C:\\Users\\13342\\source\\repos\\PodcastSearch\\transcripts.csv", sep="^")

# Display the first few rows
print(df.head())

# Display the data types of each column
print(df.dtypes)
