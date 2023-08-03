from bs4 import BeautifulSoup
import openpyxl
import requests
web = requests.get('https://www.chittorgarh.com/report/ipo_report_listing_day_gain/98/')
topics = []
soup = BeautifulSoup(web.text)
alpha = soup.findAll('tr')
for content in alpha:
    rst = content.findAll('td')
    head = [j.text for j in rst]
    try:
        del head[1]
        del head[3:7]
    except:
        continue
    if(len(head) ==  9):
        topics.append(head)
        print(head)
        book = openpyxl.Workbook()
rbd = book.active
rbd.append(["Issuer Company", "Issue Price", "Issue Price (Rs Cr)", "Total", "Open Price", "Low Price", "High Price", "Close Price", "% Change"])
for content in topics:
    rbd.append(content)
book.save("ansh.xlsx")