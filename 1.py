import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req

src = ("https://www.ptt.cc/bbs/movie/index.html")

request = req.Request(src, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
})

with req.urlopen(request) as response: 
    data = response.read().decode("utf-8") 

import bs4 
root = bs4.BeautifulSoup(data, "html.parser") 
titles = root.find_all("div", class_="title")
 
for title in titles:
    if title.a != None and "討論" in title.a.string: 
       print(title.a.string)

import email.message
msg = email.message.EmailMessage()
msg["From"] = "kueifangp@gmail.com"
msg["To"] = "kueifangp@gmail.com"
msg["Subject"] = "您要的PTT更新來ㄌ"
msg.set_content= "爬蟲的成果"

import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("kueifangp@gmail.com","password")
server.send_message(msg)
server.close()
