#This is an outdated version being kept for the commented out examples of other functions that may be needed later.
import bs4 as bs
import urllib.request
import mysql.connector
from mysql.connector import Error

CSSCLASSPOSITION = 0
RELATIVEURLPOSITION = 1

def fetchlinks(cssclass,url):
	returnMe = []
	source = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(source,'html.parser')
	for companies in soup.find_all('div', {'class' : cssclass}):
		for links in companies.find_all('a'):
			linkArray = []
			linkArray.append(cssclass)
			linkArray.append(links.text)
			linkArray.append(links.get('href'))
			returnMe.append(linkArray);
			## returnMe.append(cssclass+','+links.text+',https://en.wikipedia.org'+links.get('href'))
	return returnMe

# def fetchnames(url):
# 	subsource = urllib.request.urlopen(url).read()
# 	subsoup = bs.BeautifulSoup(source,'html.parser')
# 	for companies in soup.find_all('div', {'class' : cssclass}):
# 		for links in companies.find_all('a'):
# 			linkArray = []
# 			linkArray.append(cssclass)
# 			linkArray.append(links.text)
# 			linkArray.append(links.get('href'))
# 			returnMe.append(linkArray);
# 			## returnMe.append(cssclass+','+links.text+',https://en.wikipedia.org'+links.get('href'))
# 	return returnMe

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_anime_companies').read()
soup = bs.BeautifulSoup(source,'html.parser')

db = mysql.connector.connect(host="localhost",user="root",passwd="access01" , db = "wiki")

print("====Animation Studios====")
studiolinks = fetchlinks('Studio_List','https://en.wikipedia.org/wiki/List_of_anime_companies')
print(studiolinks)
print("studios were inserted into db")

cur = db.cursor()
cur.executemany("""
	INSERT IGNORE INTO studios (type, name, url)
	VALUES(%s, %s, %s)
""", studiolinks)
db.commit()

print("====Producers====")
producerlinks = fetchlinks('Producer_List','https://en.wikipedia.org/wiki/List_of_anime_companies')
print(producerlinks)
print("production companies were inserted into db")

cur = db.cursor()
cur.executemany("""
	INSERT IGNORE INTO companies (type, name, url)
	VALUES(%s, %s, %s)
""", producerlinks)
db.commit()

# Grab URLs from studios table

domain = ('https://en.wikipedia.org')
cursor = db.cursor()

number_of_rows = cursor.execute("SELECT url FROM `studios` WHERE id = 9");

result = cursor.fetchall()
for row in result:
	print(domain,row)


subsource = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_anime_companies').read()
subsoup = bs.BeautifulSoup(subsource,'html.parser')




# ====================================================================
# print('====Animation Studios====')
# for studios in soup.find_all('div', {'class' : 'Studio_List'}):
# 	for links1 in studios.find_all('a'):
# 		print(links1.text+',https://en.wikipedia.org'+links1.get('href'))
#
# print('====Producers:====')
# for producers in soup.find_all('div', {'class' : 'Producer_List'}):
# 	for links2 in producers.find_all('a'):
# 		print(links2.text+',https://en.wikipedia.org'+links2.get('href'))
# # ====================================================================
#
#
# source = urllib.request.urlopen('https://en.wikipedia.org'+links.get('href')).read()
# soup = bs.BeautifulSoup(source,'html.parser')
#
# eng = soup.find_all('b')
#
# kana = soup.find_all('span', {'lang' : 'ja'})
#
# romaji = soup.find_all('i')
#
# for index in range(len(kana)):
# 	if index == 0:
# 		print("1st kana: "+kana[index].text)
# 	elif index == 1:
# 		print("2nd kana: "+kana[index].text)
# 	else:
# 		print("current index"+str(index))
#
# # ==============================
#
#
#
# for url in line.find_all('a'):
# 	print(url.get('href'))
#
#
# title of the page
# print(soup.title)
#
# get attributes:
# print(soup.title.name)
#
# get values:
# print(soup.title.string)
#
# beginning navigation:
# print(soup.title.parent.name)
#
# getting specific values:
# print(soup.p)
#
# print(soup.find_all('p'))
#
# for paragraph in soup.find_all('p'):
# 	print(paragraph.string)
# 	print(str(paragraph.text))
#
# for url in soup.find_all('a'):
# 	print(url.get('href'))
#
# # Find the div with the company name in the infobox - may have romaji+kana names together
# for caption in soup.find_all('caption', class_='fn org'):
# 	print(caption.text)
#
#
# eng = soup.find_all('b')
#
# kana = soup.find_all('span', {'lang' : 'ja'})
#
# romaji = soup.find_all('i')
#
# for index in range(len(kana)):
# 	if index == 0:
# 		print("1st kana: "+kana[index].text)
# 	elif index == 1:
# 		print("2nd kana: "+kana[index].text)
# 	else:
# 		print("current index"+str(index))
#
#
# print("1st eng: "+str(eng[0].text))
# print("1st kana: "+str(kana[0].text))
# print("1st romaji: "+str(romaji[0].text))
# print("2nd eng: "+str(eng[1].text))
# print("2nd kana: "+str(kana[1].text))
# print("2nd romaji: "+str(romaji[1].text))
# print("2nd eng: "+str(eng[2].text))
# print(eng.text)
