import feedparser
import time
import os, sys
from future import Future
from LittleFeedsOnMongo import Newsfeed
from pymongo import MongoClient
from datetime import datetime
from stat import *
from DBConfig import *

client = MongoClient()
db = client[dbName]
newsfeeds = db[collectionName]

class Crawler(object):
	"""docstring for Crawler
	the main spider class that execute the 
	actual fetching of feed from all the feedseeds
	currently are single threaded, loop through seeds
	which later would be more threaded and do fetching 
	ASYNCHRONIZINGLY.
	"""
	def __init__(self, channels_filename):
		super(Crawler, self).__init__()
		# self.seeds = seeds
		self.hush = True
		self.minutes = 5
		self.channels = []
		self.channels_mtime = 0.0
		self.channels_filename = channels_filename
		self.updateChannelList()

	def saveFeed(self,item0):
		# print "SUMMARY: %s\n" %(item0["summary"])
		# print "HISTORY : %s" %(item0["wiki_history"])
		# print "DIFF : %s" %(item0["wiki_diff"])		pass
		#Save it somehow.
		feedstore = Newsfeed()
		feedstore.guid = "xxx0jx0jx000"
		feedstore.title = item0["title"]
		feedstore.link = item0["link"]
		feedstore.descript = item0["description"]
		feedstore.editStatus = 0;
		feedstore.editorId = 0;	
		# feedstore.source = ""
		# feedstore.rssid = ""
		# feedstore.editorMemo = ""
		# repeated feeds
		repeated = newsfeeds.find_one({"title":item0["title"], "link":item0["link"]})
		# print "THere existed some like %s of the same guid" %(repeated)
		if repeated:
			print "XXXXXXXXXX Existed GUID:%s" %("xxxx")
			return 0;
		else :
			_id = feedstore.save()
			print "OOOOOOOOOO NewLy!!!!!!!: %s\n" %(_id)
			print "TITLE: %s" %(item0["title"])
			print "LINK : %s" %(item0["link"])
			# print "DESCP: %s\n" %(item0["description"])
			# print "GUID: %s"  %(item0["link"])
			return 1;

	def crawl(self):
		feed = feedparser.parse(self.channels[0])
		items = feed["items"]
		print "items : %d" %(len(items))
		# print items[0]
		minutes = 0
		for x in xrange(0,len(items)):
			item0 = items[x]
			minutes += self.saveFeed(item0)
		if len(items):
			newly = float(minutes)/float(len(entries))
			# self.minutes =5*(1-newly)
		
		return self.minutes

	def spide(self):
		"""
		The multi-threaded version of crawl
		"""
		future_calls = [Future(feedparser.parse,rss_url) for rss_url in self.channels]
		# block until they are all in
		feeds = [future_obj() for future_obj in future_calls]
		entries = []
		for feed in feeds:
		    entries.extend(feed[ "items" ] )
		# sorted_entries = sorted(entries, key=lambda entry: entry["date_parsed"])
		# sorted_entries.reverse() # for most recent entries first
		# for item in sorted_entries:
		minutes = 0
		for item in entries:
			minutes += self.saveFeed(item)
		print "NewLy Fetched %d Feeds between %d entries" %(minutes, len(entries))
		if len(entries):
			newly = float(minutes)/float(len(entries))
			self.minutes =5*(1-newly)
		print "%s : Gonnoa have a %d minutes SNAP" %(datetime.now(), self.minutes)
		return self.minutes

	def creep(self, spider):
		"""
		"""
		# We use APScheduler for some crontab style jobs
		# We need a timer, to schedule the spider for auto crawling.
		# Other hand, we also must have the ability to manually crawling.
		self.minutes = 5
		while self.hush:
			self.minutes = self.spide()
			self.updateChannelList()
			time.sleep(self.minutes*60)
			print "%d MINUTES, wake up and crawl ....\n" %(self.minutes)

	def rest(self):
		self.hush = False;

	def updateChannelList(self):
		d = {}
		a = []
		# a.extend(google_news_rss,smzdm_rss)
		pathname = self.channels_filename
		mtime = os.stat(pathname).st_mtime
		if self.channels_mtime!=mtime:
			self.channels_mtime = mtime
			with open(pathname) as f:
				# i = 1
			    for line in f:
			       	(key, val) = line.split("==")			       	
			       	print "channel lines :%s:%s" %(key, val)
			       	d[key] = val
			       	a.append(val.lstrip())
			self.channels = a
			print "Fetched from FS %s" %(a)

if __name__ == '__main__':	
	print("Main...ing")
	cawler = Crawler("channels")
	cawler.creep(0)



