from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup   
def Trans_Jp(text):
    
    options = Options()
    options.add_argument("--disable-notifications")

    '''selenium搜尋翻譯並輸入(translate to jp)'''
    PATH="D:/陳睿倬/program/Joyce/chromedriver.exe"
    chrome = webdriver.Chrome(PATH, chrome_options=options)
    chrome.get("https://translate.google.com.tw/?hl=zh-TW&sl=auto&tl=ja&op=translate")
    time.sleep(2)
    input=chrome.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
    input.send_keys(text)              #/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea
    #時間優化
    element = WebDriverWait(chrome, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "eyKpYb"))
    )
    time.sleep(3)
    '''beautifulsoup解析、取得翻譯'''
    soup=BeautifulSoup(chrome.page_source,"html.parser")

    print(text+"的日文是:")

    jp=soup.find('span',{'jsname':'W297wb'})
    if jp:
        print(jp.getText())

    chrome.quit()