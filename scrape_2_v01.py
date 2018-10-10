#The purpose of this app is to loop through all the urls for production and animation studios in the database and scrape additional info about each one (e.g. dates in operation, official website, save logo locally and record location in DB, etc.) and insert that info into the existing records. It will also parse the lists works of those companies into a new table and link the originating company to the records for their works.

import bs4 as bs
import urllib.request
import mysql.connector
from mysql.connector import Error

# Connect to DB
def get_db_client():
	return mysql.connector.connect(host="localhost",user="root",passwd="access01" , db = "wiki")

# get list of urls
def fetchurllist(table):
	db = get_db_client()  # get a connection to the database
	SELECT url FROM (table)

# for each in list of urls, do the soup
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

# store the soup results in works table
def store_pagedata(fetchurllist):
	db = get_db_client()  # get a connection to the database
	for data in fetch_links_data: # iterate over the dictionaries that are passed into this function (wiki_data)
		try: # if something bad happens dont crash
##			links = fetchurllist(data.get('cssclass'),data.get('url')) #call the fecthlinks function with the current dictionaries (cssclass, and url)
			cur = db.cursor() # open a db cursor
			cur.executemany("INSERT IGNORE INTO {} (type, name, url) VALUES(%s, %s, %s)".format(data.get('table')), links) #insert data into the table provided by the wiki_dictionary field "table"
			db.commit() # commit that sucker
		except Exception as e: # if anything goes wrong (in the try block), execute the code in the except block and continue
			print('Something has gone wrong: {}, {}, {}', data.get('cssclass'),data.get('url'),data.get('table'))
			print('See Exception: {}', str(e))
	db.close(); # close the connection
