#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the website
driver.get("https://nhentai.net/g/516162/")

# Create a directory to save images
if not os.path.exists("images"):
    os.makedirs("images")

# Getting all thumb-container elements
thumb_containers = driver.find_elements(By.CLASS_NAME, "thumb-container")

# Iterate through each thumb-container and download the images
for index, thumb_container in enumerate(thumb_containers):
    img_element = thumb_container.find_element(By.TAG_NAME, "img")
    img_url = img_element.get_attribute("src")

    # Download the image
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(f"images/thumbnail_{index}.jpg", "wb") as file:
            file.write(response.content)
        print(f"Image {index} downloaded successfully.")
    else:
        print(f"Failed to download image {index}.")

# Close the driver
driver.quit()
