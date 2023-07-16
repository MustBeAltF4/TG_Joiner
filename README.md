# Telegram Chat Joiner

This script allows you to join multiple Telegram chats using multiple Telegram accounts simultaneously. It utilizes the `telethon` library to interact with the Telegram API.

## Prerequisites

- Python 3.6 or above
- `telethon` library (can be installed via `pip install telethon`)

## Getting Started

1. Clone the repository and navigate to the project directory.

2. Install the required dependencies by running the following command:

   ```
   pip install telethon
   ```

3. Open the `main.py` file in a text editor.

4. Replace the placeholder values in the following variables with your own information:

   - `api_id`: Your Telegram API ID. Obtain this value by creating a Telegram application at the [Telegram API Development Tools](https://my.telegram.org/apps) page.
   - `api_hash`: Your Telegram API hash. Obtain this value from the same page where you obtained the API ID.
   - `session_file`: The name of the session file to save the user sessions. You can choose a custom name for this file.

5. Create two text files, `accounts.txt` and `chats.txt`, and populate them with the Telegram accounts and chats you want to join, respectively. Each entry should be on a separate line.

   Example `accounts.txt`:
   ```
   user1
   user2
   user3
   ```

   Example `chats.txt`:
   ```
   chat1
   chat2
   chat3
   ```

6. Run the script by executing the following command:

   ```
   python join_chats.py
   ```

   The script will iterate over each Telegram account in `accounts.txt` and join the chats specified in `chats.txt`. A success or failure message will be displayed for each attempt.

   **Note:** The script will wait for 1 second between joining each chat to avoid triggering anti-spam measures. You can adjust the delay as needed.

7. After the script finishes executing, you can check the console output for any error messages or failed attempts.

## Important Notes

- Ensure that you have the necessary permissions to join the specified chats with the provided Telegram accounts.
- Take into account any rate limits or anti-spam measures imposed by Telegram. Adjust the delay between joining chats accordingly to avoid being blocked.
- It's recommended to use multiple Telegram accounts to distribute the load and minimize the risk of exceeding rate limits.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

Feel free to contribute to the project by submitting issues or pull requests.
