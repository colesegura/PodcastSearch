import psycopg2

# Connect to the database
connection = psycopg2.connect(
    host="cwspodcastsearchdb.postgres.database.azure.com",
    database="postgres",
    user="colesegura",
    password=";!L5?q6$NKC}N]4"
)
cursor = connection.cursor()

# Create the new table
cursor.execute("""
    CREATE TABLE podcast_data.episodes_transcripts (
        id SERIAL PRIMARY KEY,
        podcast_id INTEGER,
        title TEXT,
        date DATE,
        transcript TEXT
    )
""")

# Merge the data from the transcripts and episodes tables into the new table
cursor.execute("""
    INSERT INTO podcast_data.episodes_transcripts (podcast_id, title, date, transcript)
    SELECT e.podcast_id, e.title, e.date, t.transcript
    FROM podcast_data.episodes e
    JOIN podcast_data.transcripts t ON e.id = t.episode_id
""")

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()
