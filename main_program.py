'''Gmail-api'''
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
'''search'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
'''trans'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''vedio'''
from download_vedio import DownLoad_Vedio


import time


from time import gmtime
from record_voice_func import record_voice
from search import Search
from trans_Chn import Trans_Chn
from trans_Eng import Trans_Eng
from trans_Jp import Trans_Jp
from Gmail_api import Gmail_api

text = record_voice()
print(text)
#https://chromedriver.chromium.org/
if "搜尋" in text:
    text=text.replace("搜尋",'')
    print(text)
    Search(text)
if "翻譯" and "中文" in text:
    text=text.replace("翻譯",'')
    text=text.replace("中文",'')
    print(text)
    Trans_Chn(text)
elif "翻譯" and "英文" in text:
    text=text.replace("翻譯",'')
    text=text.replace("英文",'')
    print(text)
    Trans_Eng(text)
elif "翻譯" and "日文" in text:
    text=text.replace("翻譯",'')
    text=text.replace("日文",'')
    print(text)
    Trans_Jp(text)
elif ("寄" in text) or ("郵件" in text):
    Gmail_api()
elif ("下載" in text and "音樂" in text):
    DownLoad_Vedio()
