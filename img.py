import random
import requests
import os
import time

# Create a set to store used image names
used_names = set()

# Number of images you want to download
num_images = 1000  # You can change this number as needed

for _ in range(num_images):
    # Generate a unique random name
    while True:
        img_name = random.randint(1000, 9999)
        if img_name not in used_names:
            used_names.add(img_name)
            break
    
    # Construct the file path and URL
    file_path = f"avatars/{img_name}.jpg"
    url = "https://thispersondoesnotexist.com"
    
    # Download and save the image
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {file_path}")
    else:
        print(f"Failed to download image from {url}")
        

