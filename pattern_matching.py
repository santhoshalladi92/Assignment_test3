from pymongo import MongoClient
import scrapy

urls = []
titles=[]
#connecting to mongo
try:
	client = MongoClient()
except Exception, e:
	print "not connected"

db = client.linkdb
collection = db.linkslist
sites = collection.find()
index = 0

for site in sites:
	urls.insert(index, site['link'].encode('utf-8'))
	index = index + 1


db = client.linkdb
collection = db.linksdata1
site_info=collection.find()

i=0

for info in site_info:
    titles.insert(i,info['name']+info['address'].encode('utf-8'))
    i=i+1

def remove_space(str):
    str=str.split(" ")
    me=""
    for x in str:
        me=me+x
    return me

url_count=0
title_count=0
for url in urls:
    url=url.split("/")[4]
    url=url.split("-")
    title_count=0
    for title in titles:
        title=title.split(",")
        me=""
        for x in title:
            me=me+x
        title=me
        title=remove_space(title)
        count=0
        i=0
        for x in url:
            if x in title:
                count=count+1
            i=i+1
        if count is i:
            print titles[title_count]+ " : " +urls[url_count]
        title_count=title_count+1
    url_count=url_count+1
