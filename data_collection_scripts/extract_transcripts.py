import requests
from bs4 import BeautifulSoup

# Open the file in read mode ('r')
with open('episode_urls.txt', 'r') as file:
    # Read the URLs from the file
    episode_urls = [line.strip() for line in file]

for url in episode_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the transcript on the page and extract it
    # The details of this will depend on the structure of the webpage
    # For example, if the transcript is in a <div> with class "transcript", you could do:
    transcript_div = soup.find("div", class_="transcript")
    transcript = transcript_div.text if transcript_div else "No transcript found"

    print(transcript)
