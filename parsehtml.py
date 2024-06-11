import requests
from bs4 import BeautifulSoup
import os


# Function to download a file
def download_file(url, directory):
    local_filename = os.path.join(directory, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return local_filename


# Function to get all links from a webpage
def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links


# Main function to open links and download files
def main(url, download_directory):
    links = get_links(url)
    for link in links:
        try:
            absolute_link = requests.compat.urljoin(url, link)
            if absolute_link.endswith('.pdf') or absolute_link.endswith('.zip'):
                print("Downloading:", absolute_link)
                download_file(absolute_link, download_directory)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    # Specify the URL of the website you want to scrape
    website_url = "https://msrusu.weebly.com/r_calcab---class-docs.html"

    # Specify the directory where you want to save downloaded files
    download_directory = "ref/classdocs"
    os.makedirs(download_directory, exist_ok=True)

    # Call the main function
    main(website_url, download_directory)
