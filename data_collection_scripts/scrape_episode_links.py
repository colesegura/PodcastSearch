import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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

# Print the URLs
for url in episode_urls:
    print(url)

# Open a new file in write mode ('w')
with open('episode_urls.txt', 'w') as file:
    # Write each URL to the file
    for url in episode_urls:
        file.write(url + '\n')
