import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse, urljoin
from urllib.request import urlretrieve
import re

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_images(url, folder_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for img in img_tags:
        try:
            img_url = img['src']

            if not urlparse(img_url).scheme:
                img_url = urljoin(url, img_url)

            filename = os.path.basename(urlparse(img_url).path)
            filename = sanitize_filename(filename)

            filepath = os.path.join(folder_path, filename)

            urlretrieve(img_url, filepath)
            print(f"Downloaded {filepath}")
        except Exception as e:
            print(f"Error downloading image: {e}")

url = str(input("URL: "))
folder_path = 'downloaded_images'
download_images(url, folder_path)