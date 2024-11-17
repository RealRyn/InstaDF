import instaloader
from datetime import datetime, timedelta
import time
import os
import shutil

# DOC.. : https://instaloader.github.io/
loader = instaloader.Instaloader()

# Log in
username = "INSERT USERNAME"
password = "INSERT PASSWORD"
loader.login(username, password)

# List of usernames to download their stories / Maybe will become input.
target_users = ["instagram", "israel_bidur"]

# Time period for one week
start_date = datetime.now()
end_date = start_date + timedelta(days=7)

print(f"Started at {start_date}. Will run until {end_date}.")

while datetime.now() < end_date:
    for user in target_users:
        try:
            print(f"Downloading stories for {user}...")
            profile = instaloader.Profile.from_username(loader.context, user)

            # Get stories for the user
            for story in loader.get_stories(userids=[profile.userid]):
                for item in story.get_items():
                    # Format the date of the story
                    story_date = item.date.strftime('%Y-%m-%d')

                    # Create a subfolder for the user and date
                    base_folder = os.path.join(os.getcwd(), user)
                    target_folder = os.path.join(base_folder, story_date)
                    logs_folder = os.path.join(base_folder, "logs")
                    os.makedirs(target_folder, exist_ok=True)
                    os.makedirs(logs_folder, exist_ok=True)

                    # Temporarily set the download target folder
                    loader.dirname_pattern = target_folder

                    # Download the story item
                    loader.download_storyitem(item, target=target_folder)

                    # Move `.json.xz` files to the logs folder
                    for file in os.listdir(target_folder):
                        if file.endswith(".json.xz"):
                            shutil.move(
                                os.path.join(target_folder, file),
                                os.path.join(logs_folder, file)
                            )

            print(f"Stories for {user} downloaded successfully!")

        except Exception as e:
            print(f"Error downloading stories for {user}: {e}")

    wait_period = 79200  # In seconds
    print(f"Waiting for the next cycle... {wait_period} seconds left.")
    time.sleep(wait_period)  # 79200 = 22 hours

print("The week has ended.")
