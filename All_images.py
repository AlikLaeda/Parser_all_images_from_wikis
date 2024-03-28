# Python script for web scraping to extract data from a website
import requests
from bs4 import BeautifulSoup

def url_constructor(url):
    slice = url.split('/')
    print(f"https://millennia.paradoxwikis.com/images/{slice[3]}/{slice[4]}/{slice[5]}")
    return 'https://millennia.paradoxwikis.com/images/' + slice[3] + '/' + slice[4] + '/' + slice[5]

def download_images(url, save_directory, name):

    image_response = requests.get(url)
    if image_response.status_code == 200:
        with open(f"{save_directory}/{name}", "wb") as f:
            f.write(image_response.content)


def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
# Your code here to extract relevant data from the website
    list_imgs = soup.find_all('img')

    for one_img in list_imgs:

        one_url = one_img.get('src')
        print(one_url.find('images', 0, 10))
        if one_url.find('images', 0, 10) == 1:
            url = url_constructor(one_url)
            download_images(url, 'millennia', one_url.split('/')[5])


    
if __name__ == "__main__":
    scrape_data("https://millennia.paradoxwikis.com/Tiles")