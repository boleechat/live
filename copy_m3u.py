import os 
import requests
import base64

def main():

  token = os.environ['TOKEN'] # 获取TOKEN

  source_url = '...'
  destination_url = '...'

  response = requests.get(source_url)
  content = response.text

  # 替换内容

  content = base64.b64encode(content.encode('utf-8'))  

  headers = {
    'Content-Type': '...',
    'Authorization': f'token {token}' 
  }

  response = requests.put(destination_url, data=content, headers=headers)

  if response.status_code == 200:
    print('更新成功')
  else:
    print('更新失败')

if __name__ == '__main__':
  main()
