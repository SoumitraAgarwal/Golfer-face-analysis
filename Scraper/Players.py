# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd

url = "https://www.pgatour.com/players.html"
proxies = {
  'http': 'http://172.16.115.214:3128',
  'https': 'https://172.16.115.214:3128',
}

page = requests.get(url,proxies=proxies)

html = page.content
soup = BeautifulSoup(html,'lxml')
right_table = soup.find('div', class_='directory-select')

A=[]
B=[]

flag = 0
for row in right_table.findAll("option"):
	if(flag == 0):
		flag = 1
		continue
	else:
		A.append(row.find(text = True).encode('utf-8'))
		B.append(row["value"])
		print("Done for " + row.find(text = True))

df = pd.DataFrame({
	"Name" 	: A,
	"Url"	: B
	})

df.to_csv("Players.csv", index = False)