import requests
import os
import base64

def main():

  token = os.environ['TOKEN']

  source_url = 'https://ghproxy.com/https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/global.m3u'
  destination_url = 'https://raw.githubusercontent.com/boleechat/live/main/globe.m3u'

  response = requests.get(source_url)
  content = response.text

  # content processing

  content = base64.b64encode(content.encode('utf-8'))

  headers = {
    'Content-Type': 'text/plain; charset=utf-8',
    'Authorization': f'token {token}'
  }

  response = requests.put(destination_url, data=content, headers=headers)

  if response.status_code == 200:
    print('更新成功')
  else:
    print('更新失败')

if __name__ == '__main__':
  main()
