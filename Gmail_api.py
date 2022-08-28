

"""def record_voice():
    import speech_recognition as sr
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    txt = r.recognize_google(audio, language="zh-TW")
    return txt
"""

def Gmail_api():
    from email.mime.multipart import MIMEMultipart

    from email.mime.text import MIMEText
    from record_voice_func import record_voice

    import smtplib
    import time
    content = MIMEMultipart()

    
    print("郵件標題---1")

    time.sleep(1)
    subtext = record_voice()
    print(subtext)
    content["subject"] = subtext  # 郵件標題

    #text = input("寄件者: ")
    content["from"] =  "yourGmail@gmail.com" #寄件者

    text = input("收件者: ")
    content["to"] = text  # 收件者

    time.sleep(1)

    print("內容--1")
    time.sleep(1)

    text = record_voice()
    print(text)
    content.attach(MIMEText(text))


    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("ricky93093020160616@gmail.com", "lxssvacfqqjpbfbv")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)


#Gmail_api()



