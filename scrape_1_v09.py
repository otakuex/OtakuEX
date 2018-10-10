#The purpose of this app is to scrape a list of production and animation studios and their individual page URLs (for deeper scraping in later app) and store it in a database.
import bs4 as bs
import urllib.request
import mysql.connector
from mysql.connector import Error

#CSSCLASSPOSITION = 0
#RELATIVEURLPOSITION = 1

wiki_data = [
	{
		'cssclass': 'Studio_List',
		'url': 'https://en.wikipedia.org/wiki/List_of_anime_companies',
		'table': 'studios'
	},
	{
		'cssclass': 'Producer_List',
		'url': 'https://en.wikipedia.org/wiki/List_of_anime_companies',
		'table': 'companies'
	}
]

def get_db_client():
	return mysql.connector.connect(host="localhost",user="root",passwd="access01" , db = "wiki")

def read_from_url(url):
	return urllib.request.urlopen(url).read()

def fetchlinks(cssclass,url):
	returnMe = []
	source = read_from_url(url)
	soup = bs.BeautifulSoup(source,'html.parser')
	for companies in soup.find_all('div', {'class' : cssclass}):
		for links in companies.find_all('a'):
			linkArray = []
			linkArray.append(cssclass)
			linkArray.append(links.text)
			linkArray.append(links.get('href'))
			returnMe.append(linkArray);
	return returnMe

def store_links(fetch_links_data):
	db = get_db_client() # get a connection to the database
	for data in fetch_links_data: # iterate over the dictionaries that are passed into this function (wiki_data)
		try: # if something bad happens dont crash
			links = fetchlinks(data.get('cssclass'),data.get('url')) #call the fecthlinks function with the current dictionaries (cssclass, and url)
			cur = db.cursor() # open a db cursor
			cur.executemany("INSERT IGNORE INTO {} (type, name, url) VALUES(%s, %s, %s)".format(data.get('table')), links) #insert data into the table provided by the wiki_dictionary field "table"
			db.commit() # commit that sucker
		except Exception as e: # if anything goes wrong (in the try block), execute the code in the except block and continue
			print('Something has gone wrong: {}, {}, {}', data.get('cssclass'),data.get('url'),data.get('table'))
			print('See Exception: {}', str(e))
	db.close(); # close the connection

# get list of urls from studios table, loop through them to read the pages, parse the data and insert into works table


# start of app

store_links(wiki_data)
