# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd
import shutil

df = pd.read_csv("Players.csv")

print("Read complete")


url = "https://www.pgatour.com"
proxies = {
  'http': 'http://172.16.115.214:3128',
  'https': 'https://172.16.115.214:3128',
}

for i in range(len(df)):
	print(i)
	url_temp = url+df['Url'][i]
	while(True):
		print("Getting page for " + df['Name'][i])
		try:
			page = requests.get(url_temp,proxies=proxies)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break

	html = page.content
	soup = BeautifulSoup(html,'lxml')
	
	Nat = soup.find('img', class_="photo")
	while(True):
		try:
			response = requests.get("https://pga-tour-res.cloudinary.com/image/upload/" + Nat['data-src'], stream=True,proxies=proxies)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break
	with open('../Pictures/'+df['Name'][i]+'.png', 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response