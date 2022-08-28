

def Search(text):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    #import time
    from bs4 import BeautifulSoup
    
    options = Options()
    options.add_argument("--disable-notifications")
    '''selenium搜尋並輸入'''
    PATH="D:/陳睿倬/program/Joyce/chromedriver.exe"
    chrome = webdriver.Chrome(PATH, chrome_options=options)
    chrome.get("https://www.google.com/")
                                      #/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
    sear=chrome.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    sear.send_keys(text)
    click=chrome.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
    click.submit()
    #time.sleep(2)
    '''beautifulsoup取得標題'''
    soup=BeautifulSoup(chrome.page_source,"html.parser")
    titles=soup.find_all('div',{'class':'yuRUbf'})
    for title in titles:
        link=title.find('cite',{'role':'text'})
        post=title.find('h3',{'class':'LC20lb MBeuO DKV0Md'})
        if post:
            print(post.getText())
        if link:
            print(link.getText())
        print()
        
    chrome.quit()






