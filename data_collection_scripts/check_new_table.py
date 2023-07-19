import psycopg2

# Connect to the database
connection = psycopg2.connect(
    host="cwspodcastsearchdb.postgres.database.azure.com",
    database="postgres",
    user="colesegura",
    password=";!L5?q6$NKC}N]4"
)
cursor = connection.cursor()

# Query the first 10 rows from the new table
cursor.execute("""
    SELECT * FROM podcast_data.episodes_transcripts LIMIT 10
""")

# Fetch the results
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
cursor.close()
connection.close()
