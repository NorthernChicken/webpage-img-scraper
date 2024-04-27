import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse, urljoin
from urllib.request import urlretrieve

def download_images(url, folder_path):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all img tags
    img_tags = soup.find_all('img')
    
    # Create folder to save images if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Download each image
    for img in img_tags:
        img_url = img['src']
        
        # If the image URL is relative, convert it to absolute URL
        if not urlparse(img_url).scheme:
            img_url = urljoin(url, img_url)
        
        # Get the filename from the URL
        filename = os.path.join(folder_path, os.path.basename(img_url))
        
        # Download the image
        urlretrieve(img_url, filename)
        print(f"Downloaded {filename}")

# Example usage
url = 'https://youtube.com'  # Replace with the URL of the webpage
folder_path = 'downloaded_images'  # Folder where images will be saved
download_images(url, folder_path)
