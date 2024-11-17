
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
**better readme coming soon.**
