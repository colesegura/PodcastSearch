import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import psycopg2

base_url = "https://podscripts.co"
url = urljoin(base_url, "/podcasts/duncan-trussell-family-hour/")

# Use a set to store the URLs
episode_urls = set()

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <a> tags with href attribute starting with "/podcasts/duncan-trussell-family-hour/"
    episode_links = soup.find_all("a", href=lambda href: href and href.startswith("/podcasts/duncan-trussell-family-hour/"))

    for link in episode_links:
        episode_urls.add(urljoin(base_url, link['href']))

    # Find the link to the next page
    next_page_link = soup.find("a", class_="nextposts-link")
    url = urljoin(base_url, next_page_link['href']) if next_page_link else None

# Connect to the database
connection = psycopg2.connect(
    host="cwspodcastsearchdb.postgres.database.azure.com",
    database="postgres",
    user="colesegura",
    password=";!L5?q6$NKC}N]4"
)
cursor = connection.cursor()

# Define the batch size
batch_size = 10

# For each batch of episode URLs
for i in range(0, len(episode_urls), batch_size):
    batch = list(episode_urls)[i:i+batch_size]

    # For each episode URL in the batch
    for episode_url in batch:
        print(f"Processing {episode_url}...")  # Print a message before processing each URL

        # Get the episode page
        response = requests.get(episode_url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrape the episode title and date
        title_element = soup.find("title")
        title = title_element.text if title_element else None
        date_element = soup.find("span", class_="episode_date")
        date = date_element.text.replace('Episode Date: ', '') if date_element else None

        # Scrape the transcript
        transcript_elements = soup.find_all("span", class_="transcript-text")
        transcript = " ".join(element.text.strip() for element in transcript_elements)

        # Insert the episode into the episodes table
        postgres_insert_query = """ INSERT INTO podcast_data.episodes (podcast_id, title, date) VALUES (%s,%s,%s) RETURNING id"""
        cursor.execute(postgres_insert_query, (1, title, date))
        episode_id = cursor.fetchone()[0]

        # Insert the transcript into the transcripts table
        postgres_insert_query = """ INSERT INTO podcast_data.transcripts (podcast_id, transcript, episode_id) VALUES (%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (1, transcript, episode_id))

        print(f"Successfully inserted data for {episode_url}")  # Print a message after inserting the data

    # Commit the changes after each batch
    connection.commit()

# Close the connection after all batches have been processed
cursor.close()
connection.close()
