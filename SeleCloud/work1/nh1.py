from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import base64

# Replace with your actual website URL
website_url = "https://nhentai.net/g/516162"

# Create a new Chrome webdriver instance
driver = webdriver.Chrome()
driver.get(website_url)

# Wait for the image thumbnails to load
wait = WebDriverWait(driver, 10)
thumbnails = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.thumb-container a.gallerythumb img")))

# Create a directory to store the images
os.makedirs("images", exist_ok=True)

# Iterate through the image thumbnails
for i, thumbnail in enumerate(thumbnails):
    # Get the image URL
    image_url = thumbnail.get_attribute("data-src")

    # Check if it's a data URI
    if image_url.startswith('data:image/'):
        # Decode the base64 encoded image data
        header, encoded_data = image_url.split(",", 1)
        data = base64.b64decode(encoded_data)

        # Save the image
        image_name = f"image_{i + 1}.png"
        with open(os.path.join("images", image_name), "wb") as f:
            f.write(data)

        print(f"Downloaded {image_name}")
    else:
        # Download the image from the URL if it's not a data URI
        try:
            driver.get(image_url)
            # Wait for the image to load
            wait = WebDriverWait(driver, 10)
            image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.lazyload")))

            # Get the image source
            image_source = image.get_attribute("src")

            # Save the image
            image_name = f"image_{i + 1}.png"
            with open(os.path.join("images", image_name), "wb") as f:
                f.write(driver.get_screenshot_as_png())

            print(f"Downloaded {image_name}")

        except Exception as e:
            print(f"Error downloading image {i + 1}: {e}")

# Close the browser
driver.quit()