import psycopg2

try:
    connection = psycopg2.connect(
        host="cwspodcastsearchdb.postgres.database.azure.com",
        database="postgres",
        user="colesegura",
        password=";!L5?q6$NKC}N]4"
    )

    cursor = connection.cursor()
    
    postgres_insert_query = """ INSERT INTO podcast_data.episodes (id, podcast_id, title, date) VALUES (%s,%s,%s,%s)"""
    episodes = [(1, 1, "Test Title", "2023-07-08"), (2, 2, "Test Title2", "2023-07-09")]

    cursor.executemany(postgres_insert_query, episodes)

    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into episodes table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into episodes table", error)

finally:
    # closing database connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
