import requests
from bs4 import BeautifulSoup as bs
import html5lib
from pprint import pprint
import json

def paytm_pickle_href():
	href = []
	for i in range(1,18):
		url = "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page={}".format(i)

		data = requests.get(url).text
		data = bs(data, 'html5lib')
		data = data.find('div',{'class': '_1LZ3'})
		data = data.find('div', {'class': '_3RA-'})
		
		for pickle_a in data.find_all('a'):
			pickle_href = pickle_a.get('href')
			pickle_href = 'https://paytmmall.com'+ pickle_href 
			href.append(pickle_href)
	return href

def pickle_data(href):
	for url in range(len(href)):
		pickles_data = requests.get(href[url]).text
		pickles_data = bs(pickles_data, 'html5lib')
		pickle_name = pickles_data.find('h1', {'class': 'NZJI'}).text
		print(pickle_name)
		pickle_img = pickles_data.find('img', {'class': '_3v_O'})
		pickle_img = pickle_img.get('src')
		print(pickle_img)
		pickle_mrp = pickles_data.find('div', {'class': '_2LVL'}).text
		print(pickle_mrp)
href = paytm_pickle_href()
pickle_data(href)