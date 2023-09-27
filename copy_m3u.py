import requests
import base64

def main():

  source_url = 'https://ghproxy.com/https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/global.m3u'
  destination_url = 'https://raw.githubusercontent.com/boleechat/live/main/globe.m3u'

  response = requests.get(source_url)
  content = response.text

  # 替换内容

  content = content.replace(content.split('\n')[0], '#EXTM3U')
  content = content.replace('https://cntv.sbs/tv?auth', 'https://www.szqcom.repl.co/PLTV/tivihk.php?url=https://cntv.sbs/tv?auth')
  #print(content)
  # base64编码content
  content = base64.b64encode(content.encode('utf-8'))
  
  headers = {'Content-Type': 'text/plain; charset=utf-8',
             'Authorization': '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'}

  response = requests.put(destination_url, data=content, headers=headers)

  if response.status_code == 200:
    print('更新成功')
  else:
    print('更新失败')

if __name__ == '__main__':
  main()
