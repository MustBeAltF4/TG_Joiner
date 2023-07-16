from telethon.sync import TelegramClient
import time

from telethon.tl.functions.messages import ImportChatInviteRequest

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
session_file = 'session'


def join_chat(client, chat):
    try:
        client(ImportChatInviteRequest(chat))
        print(f"Joined chat: {chat}")
    except Exception as e:
        print(f"Failed to join chat: {chat}")
        print(f"Error: {str(e)}")


with open('accounts.txt', 'r') as accounts_file:
    accounts = accounts_file.read().splitlines()

with open('chats.txt', 'r') as chats_file:
    chats = chats_file.read().splitlines()

for account in accounts:
    client = TelegramClient(f'sessions/{account}', api_id, api_hash)
    client.start()
    for chat in chats:
        join_chat(client, chat)
        time.sleep(1)
    client.disconnect()
