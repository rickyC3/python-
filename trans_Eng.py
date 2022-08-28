from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup  

def Trans_Eng(text):

    options = Options()
    options.add_argument("--disable-notifications")

    '''selenium搜尋翻譯並輸入(translate to eng)'''
    PATH="D:/陳睿倬/program/Joyce/chromedriver.exe"
    chrome = webdriver.Chrome(PATH, chrome_options=options)
    chrome.get("https://translate.google.com.tw/?hl=zh-TW&tab=TT&sl=auto&tl=en&op=translate")
    input=chrome.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
    input.send_keys(text)              #/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea
    #時間優化
    #element = WebDriverWait(chrome, 5).until(
    #    EC.presence_of_element_located((By.CLASS_NAME, "eyKpYb"))
    #)
    time.sleep(3)
    '''beautifulsoup解析、取得翻譯'''
    soup=BeautifulSoup(chrome.page_source,"html.parser")

    results=soup.find_all('div',{'class':'KnIHac'})

    print(text+"的英文有:")
    for result in results:
        eng = result.find('span',{'class':'kgnlhe'})
        eng2 =soup.find('span',{'jsname':'W297wb'})
        if eng:
            print(eng.getText())
        if eng2:
            print(eng2.getText())

    chrome.quit()