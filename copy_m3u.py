import os
import requests

def main():
    source_url = 'https://ghproxy.com/https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/global.m3u'
    destination_url = 'https://raw.githubusercontent.com/boleechat/live/main/globe.m3u'
    
    # 发送GET请求获取原始m3u文件内容
    response = requests.get(source_url)
    content = response.text
    
    # 替换第一行为#EXTM3U
    content = content.replace(content.split('\n')[0], '#EXTM3U')
    
    # 将包含"https://cntv.sbs/tv?auth"的内容替换为"https://www.szqcom.repl.co/PLTV/tivihk.php?url=https://cntv.sbs/tv?auth"
    content = content.replace('https://cntv.sbs/tv?auth', 'https://www.szqcom.repl.co/PLTV/tivihk.php?url=https://cntv.sbs/tv?auth')
    
    
    # 打印源文件内容  
    print(content)

    # 替换操作
    # ...

       # 将修改后的内容写入临时文件
    #with open('globe.m3u', 'w') as file:
        #file.write(content)
    
    # 提交临时文件到GitHub
    headers = {
        'Authorization': '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',
    }
    #files = {
        #'file': ('globe.m3u', open('globe.m3u', 'rb')),
    #}
   response = requests.put(destination_url, data=content, headers=headers)
    
    if response.status_code == 200:
      print('更新成功')
    else:
      print('更新失败')

if __name__ == '__main__':
    main()
