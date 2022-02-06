import requests
import time

# CONFIGURATION
channel_id = raw_input("Channel ID: ")
discord_user_token = raw_input("User Token: ")

headers = {
    'authority': 'discord.com',
    'content-length': '0',
    'x-super-properties': 'eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkRpc2NvcmQgQ2xpZW50IiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X3ZlcnNpb24iOiIwLjAuMjYzIiwib3NfdmVyc2lvbiI6IjE5LjYuMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo4NjkxNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=', # This is a JWT Token for letting Discord's API know that the client is using MacOS 64-Bit.
    'authorization': '{}'.format(discord_user_token),
    'accept-language': 'en-US',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.263 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
    'accept': '*/*',
    'origin': 'https://discord.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://discord.com/channels/@me/{}'.format(channel_id),
}

test_response = requests.post('https://discord.com/api/v9/channels/{}/typing'.format(channel_id), headers=headers)

if "" in test_response.content:
    print "Success!"
    while True:
        time.sleep(3)
        response = requests.post('https://discord.com/api/v9/channels/{}/typing'.format(channel_id), headers=headers)
        time.sleep(3)
else:
    print "Error!"
    print "DEBUG:\n" + test_response.content
    exit()