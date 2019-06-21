import requests
from bs4 import BeautifulSoup
from lxml import etree

page=1

url='https://www.ysts8.com/play_1836_49_1_'+str(page)+'.html'

def get_html(url):
    response=requests.get(url)
    response.encoding='gb2312'
    html_tree=etree.HTML(response.text,etree.HTMLParser())
    iframe_src=html_tree.xpath('//*[@id="play"]/@src')
    root_url='https://www.ysts8.com'
    result_url=root_url+iframe_src[0]
    print(result_url)
    response=requests.get(result_url)
    response.encoding='gb2312'
    html_tree=etree.HTML(response.text,etree.HTMLParser())
    print(response.text)
    #发现页面是通过js脚本渲染出来的，所以下面执行不成功
    audio_url=html_tree.xpath('//*[@id="jp_audio_0"]/@src')
    print(audio_url)
    return audio_url
def get_content(url,name):
    content=requests.get(url).content
    with open(name+'.mp3','wb') as m:
        m.write(content)
        m.close()
get_html(url)
