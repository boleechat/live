import os
import requests
import base64

def main():

  token = os.environ['TOKEN'] # 获取TOKEN

  source_url = 'https://ghproxy.com/https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/global.m3u'
  api_url = 'https://api.github.com/repos/boleechat/live/contents/globe.m3u'

  response = requests.get(source_url)
  content = response.text

  # 替换内容

  content = base64.b64encode(content.encode('utf-8')).decode('utf-8')

  headers = {
    'Authorization': f'token {token}' 
  }

  data = {
    "message": "update globe.m3u",
    "content": content
  }

  response = requests.put(api_url, json=data, headers=headers)
    print('Status code:', response.status_code)
    print('Response:', response.json())
  if response.status_code == 201:
    print('更新成功')
  else:
    print('更新失败')

if __name__ == '__main__':
  main()
