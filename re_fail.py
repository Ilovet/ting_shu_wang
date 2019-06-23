import requests
from selenium import webdriver
def get_url():
    with open('fail.txt','r') as f:
        while f.readline():
            #print(f.readline())
            get_audio(f.readline())
        f.close()           
def get_audio(url):
    browser=webdriver.Chrome()
    try:
        browser.get(url)
    except:
        with open('fail_log.txt','a+') as n:
            n.write(url+'^'+'打开网址失败'+'\n')
            n.close()
        print('失效网址：'+url)
        browser.close()
        return
    try:
        browser.switch_to.frame('play')
    except:
        print('没有id或class为play的ifrmae标签')
        with open('fail_log.txt','a+') as n:
            n.write(url+'^'+'没有id或class为play'+'\n')
            n.close()
        browser.close()
        return
    try:
        audio=browser.find_element_by_xpath('//*[@id="jp_audio_0"]')
    except:
        print('未找到audio标签')
        with open('fail_log.txt','a+') as n:
            n.write(url+'^'+'没找到audio标签'+'\n')
            n.close()
        browser.close()
        return
    try:    
        get_content(audio.get_attribute('src'),get_page(url))
    except:
        print('音频资源失效')
        with open('fail_log.txt','a+') as n:
            n.write(url+'^'+'获取音频资源失败'+'\n')
            n.close()
        browser.close()
        return
    browser.close()
def get_page(url):
    pages=url.split('_')
    page=pages[len(pages)-1].split('.')[0]
    return page
def get_content(url,name):
    content=requests.get(url).content
    if content==None:
        return
    with open(name+'.mp3','wb') as m:
        m.write(content)
        m.close()
get_url()