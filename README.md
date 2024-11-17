
# Instagram Story Downloader

A Python script that automates downloading Instagram Stories for selected users over a one-week period. The stories are stored locally for offline access, making it ideal for users who do not have access to their phones for extended periods.

---

## Features

- **Automatic Story Downloads**: Downloads stories from selected Instagram users for the specified time range.
- **Continuous Operation**: Runs for a full week, checking for new stories periodically.
- **Error Handling**: Logs errors without interrupting the script.
- **Local Storage**: Saves downloaded stories in organized folders by username.

---

## How It Works

1. **Login to Instagram**: The script logs into your Instagram account securely using the `instaloader` library.
2. **Select Users**: You specify a list of usernames whose stories you want to download.
3. **Weekly Monitoring**: The script fetches and saves stories periodically until a week has passed.
4. **Folder Organization**: Each user's stories are saved in a separate folder for easy access.

---

## Technologies Used

- **Python 3.8+**
- **Instaloader Library**: For interacting with Instagram's platform.
- **Datetime Module**: For handling time ranges.
- **Time Module**: For scheduling periodic checks.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/instagram-story-downloader.git
   cd instagram-story-downloader
   ```

2. Install required dependencies:
   ```bash
   pip install instaloader
   ```

3. Set up your Instagram credentials in the script:
   ```python
   username = "your_username"
   password = "your_password"
   ```

4. Add the usernames of the Instagram accounts you want to track:
   ```python
   target_users = ["username1", "username2"]
   ```

---

## Usage

1. Run the script:
   ```bash
   python story_downloader.py
   ```

2. Monitor the console output for progress and logs.

3. Check the local folders for downloaded stories:
   ```
   /username1/
   /username2/
   ```

---

## Future Enhancements

- **Cloud Storage**: Upload stories to Google Drive or AWS S3.
- **Web Interface**: Add a user-friendly dashboard for managing target users and schedules.
- **Push Notifications**: Notify users when new stories are downloaded.
- **Video Processing**: Convert downloaded stories into a weekly highlights video.

---

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with your enhancements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Disclaimer

This script is for personal use only. Ensure you comply with Instagram's [Terms of Use](https://help.instagram.com/581066165581870) when using this tool. Avoid using it for unauthorized data scraping or violating user privacy.
