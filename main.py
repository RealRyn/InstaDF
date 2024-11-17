import os
import shutil
import time

from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from datetime import datetime, timedelta
import instaloader

# Load environment variables from the .env file
load_dotenv()

# .env FILE CONTAIN THOSE VALUES !
username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")

# Check if credentials are found
if not username or not password:
    print("Error: Instagram username or password not set in the .env file.")
    exit(1)

# DOC.. : https://instaloader.github.io/
loader = instaloader.Instaloader()

# Log in
try:
    loader.login(username, password)
    print("Successfully logged into Instagram!")
except Exception as e:
    print(f"Login failed: {e}")
    exit(1)

# List of usernames to download their stories / Maybe will become input.
target_users = ["instagram", "israel_bidur"]

# AES encryption
key = get_random_bytes(32)  # AES-256 / 32-byte key
iv = get_random_bytes(16)   # (IV)

# Save the key, IV to a file
key_file_path = os.path.join(os.getcwd(), 'key.txt')
with open(key_file_path, 'wb') as key_file:
    key_file.write(key)
    key_file.write(iv)

print(f"Key saved to {key_file_path}")

# Setting a week
start_date = datetime.now()
end_date = start_date + timedelta(days=7)

print(f"Started at {start_date}. Will run until {end_date}.")

# Function to download, encrypt stories for a "specific" user
def download_stories(user):
    try:
        print(f"Downloading stories for {user}...")
        profile = instaloader.Profile.from_username(loader.context, user)

        # Get stories for the user
        for story in loader.get_stories(userids=[profile.userid]):
            for item in story.get_items():
                # Format the story date
                story_date = item.date.strftime('%Y-%m-%d')

                # Subfolders Set / Create
                base_folder = os.path.join(os.getcwd(), user) # User
                target_folder = os.path.join(base_folder, story_date)  # Date
                logs_folder = os.path.join(base_folder, "logs")  # Logs
                os.makedirs(target_folder, exist_ok=True)
                os.makedirs(logs_folder, exist_ok=True)

                # Set the download target folder
                loader.dirname_pattern = target_folder

                # Download the story item
                loader.download_storyitem(item, target=target_folder)

                # Move `.json.xz` files to the logs folder / reserved for future metadata extract
                for file in os.listdir(target_folder):
                    if file.endswith(".json.xz"):
                        shutil.move(
                            os.path.join(target_folder, file),
                            os.path.join(logs_folder, file)
                        )

                # Encrypt downloaded files and save with .enc extension (without deleting originals, for now.)
                for file in os.listdir(target_folder):
                    file_path = os.path.join(target_folder, file)
                    encrypt_file(file_path)

        print(f"Downloaded and encrypted stories for {user} successfully!")

    except Exception as e:
        print(f"Error downloading stories for {user}: {e}")


# Encrypt files using AES encryption
def encrypt_file(file_path):
    # Check if the file has already been encrypted
    if file_path.endswith(".enc"):
        print(f"Skipping encrypted file: {file_path}")
        return  # Skip if the file has already been encrypted

    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Set up AES encryption
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # AES verification
    padding_length = 16 - len(file_data) % 16
    file_data += bytes([padding_length]) * padding_length

    # Encrypting data
    encrypted_data = cipher.encrypt(file_data)

    # Save the encrypted file with a new name (.enc)
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)

    print(f"Encrypted file saved as {encrypted_file_path}")


# Main run
while datetime.now() < end_date:
    for user in target_users:
        download_stories(user)

    wait_period = 79200  # 79200 seconds = 22 hours
    print(f"Waiting for the next cycle... {wait_period} seconds left.")
    time.sleep(wait_period)  # Wait for 22 hours before the next cycle

print("The week has ended.")
