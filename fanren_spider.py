import requests
from selenium import webdriver

def get_content(url,name):
    content=requests.get(url).content
    if content==None:
        return
    with open(name+'.mp3','wb') as m:
        m.write(content)
        m.close()
def main():
    for page in range(1,1632):
        url='https://www.ysts8.com/play_1836_49_1_'+str(page)+'.html'
        browser=webdriver.Chrome()
        try:
            browser.get(url)
        except:
            with open('fail.txt','a+') as n:
                n.write(url+'\n')
                n.close()
            print('失效网址：'+url)
            browser.close()
            continue
        try:
            browser.switch_to.frame('play')
        except:
            print('没有id或class为play的ifrmae标签')
            with open('fail.txt','a+') as n:
                n.write(url+'\n')
                n.close()
            browser.close()
            continue
        try:
            audio=browser.find_element_by_xpath('//*[@id="jp_audio_0"]')
        except:
            print('未找到audio标签')
            with open('fail.txt','a+') as n:
                n.write(url+'\n')
                n.close()
            browser.close()
            continue
        try:    
            get_content(audio.get_attribute('src'),str(page))
        except:
            print('音频资源失效')
            with open('fail.txt','a+') as n:
                n.write(url+'\n')
                n.close()
            browser.close()
            continue
        browser.close()
if __name__=='__main__':
    main()



