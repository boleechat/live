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

  # 获取文件信息
  response = requests.get(api_url, headers=headers)
  file_info = response.json()

  # 保存文件的SHA
  file_sha = file_info['sha']

  data = {
    "message": "update globe.m3u",
    "content": content,
    "sha": file_sha  # 使用文件的SHA
  }

  response = requests.put(api_url, json=data, headers=headers)

  if response.status_code == 201:
    print('更新成功')
    print('Status code:', response.status_code)
    print('Response:', response.json())
  else:
    print('更新失败')
    print('Status code:', response.status_code)
    print('Response:', response.json())

if __name__ == '__main__':
  main()
