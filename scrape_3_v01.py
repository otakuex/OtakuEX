#The purpose of this app is the same as the last app, but with different source table of URLs and different target data to scrape. - Loop through all the urls for works (anime titles) in the database and scrape additional info about each one (e.g. plot, run dates, episode count, director(s), writer(s), character designer(s), etc.) and insert that info into the existing records.

import bs4 as bs
import urllib.request
import mysql.connector
from mysql.connector import Error

CSSCLASSPOSITION = 0
RELATIVEURLPOSITION = 1

def get_db_client():
	return mysql.connector.connect(host="localhost",user="root",passwd="access01" , db = "wiki")
