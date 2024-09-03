from bs4 import BeautifulSoup
import requests

# def scrape_website(url):
#     # Scrape website content using Beautiful Soup
#     page = requests.get(url)

#     soup = BeautifulSoup(page.content, "html.parser")

#     # Extract relevant information
#     website_data = {"title": soup.title.text, "content": soup.get_text()}

#     return website_data


def scrape_website(url):
    # Scrape website content using Beautiful Soup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # Extract relevant information
    website_data = {"title": soup.title.text, "content": soup.get_text()}
    return website_data

