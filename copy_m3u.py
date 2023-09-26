import os
import requests
from base64 import b64encode

def main():
    source_url = 'https://ghproxy.com/https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/global.m3u'
    destination_url = 'https://api.github.com/repos/boleechat/live/contents/globe.m3u'
    access_token = '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'

    # Send GET request to retrieve the original m3u file content
    response = requests.get(source_url)
    content = response.text

    # Modify the content as needed
    # ...

    # Encode the modified content as base64
    encoded_content = b64encode(content.encode()).decode()

    # Prepare the request payload
    payload = {
        "message": "Update globe.m3u",
        "content": encoded_content
    }

    # Set the Authorization header with the access token
    headers = {
        'Authorization': f'Token {access_token}',
        'Content-Type': 'application/json'
    }

    # Send PUT request to create or update the file on GitHub
    response = requests.put(destination_url, json=payload, headers=headers)

    if response.status_code == 200:
        print('m3u file successfully updated!')
    else:
        print('Failed to update m3u file.')

if __name__ == '__main__':
    main()
