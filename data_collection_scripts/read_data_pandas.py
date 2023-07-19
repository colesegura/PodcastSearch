# import pandas as pd

# transcripts = pd.read_csv('C:/Users/13342/transcripts_202307130946.csv', delimiter='^')
# print(transcripts.head())
# import pandas as pd

# # Assuming df is your DataFrame
# print(df.isnull().sum())
import pandas as pd
import psycopg2

# Connect to the database
connection = psycopg2.connect(
    host="cwspodcastsearchdb.postgres.database.azure.com",
    database="postgres",
    user="colesegura",
    password=";!L5?q6$NKC}N]4"
)

# Create a cursor object
cursor = connection.cursor()

# Execute a query to fetch all data from your table
cursor.execute("SELECT * FROM podcast_data.transcripts")

# Fetch all the rows
rows = cursor.fetchall()

# Create a DataFrame from the rows
df = pd.DataFrame(rows, columns=['id', 'podcast_id', 'transcript', 'episode_id'])

# Now you can perform operations on df
print(df.duplicated().sum())

# Don't forget to close the connection
cursor.close()
connection.close()

