import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse, urljoin
from urllib.request import urlretrieve

def download_images(url, folder_path):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')
    print(img_tags)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    for img in img_tags:
        img_url = img['src']
        
        if not urlparse(img_url).scheme:
            img_url = urljoin(url, img_url)
        
        filename = os.path.join(folder_path, os.path.basename(img_url))
        
        urlretrieve(img_url, filename)
        print(f"Downloaded {filename}")

url = 'https://picsum.photos/'
folder_path = 'downloaded_images'
download_images(url, folder_path)
