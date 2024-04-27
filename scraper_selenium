from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def download_images(url, folder_path):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    img_tags = driver.find_elements('tag name', 'img')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    for img in img_tags:
        img_url = img.get_attribute('src')
        
        if not img_url:
            continue
        
        filename = os.path.join(folder_path, os.path.basename(img_url))
        
        with open(filename, 'wb') as f:
            f.write(requests.get(img_url).content)
        print(f"Downloaded {filename}")

    driver.quit()

url = 'https://picsum.photos/'
folder_path = 'downloaded_images' 
download_images(url, folder_path)