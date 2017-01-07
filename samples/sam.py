#!/usr/bin/python
import urllib
import lxml.html
import httplib2
import time

class crawl_web:
	
	def __init__(self,urls=[],filename="urls.txt"):
		self.urls=urls	
		self.t_urls=[]
		self.fh=open(filename,"r+")
		
	def get_links(self,url):
		connection = urllib.urlopen(url)
		dom =  lxml.html.fromstring(connection.read())

		for mlink in dom.xpath('//a/@href'):
			#print "\nLINK IS :",mlink
			#time.sleep(10)
			if mlink.startswith("/"):
				if mlink.startswith("/#"):
					#print "SKIPPED"
					continue
				elif mlink.startswith("/#"):
                        		#print "SKIPPED"
					continue
				else:
					#print url+link
					#These are self reference urls 
					if url+mlink not in self.urls:
						#print "URL:",url+mlink
						self.urls.append(url+mlink)
						##self.fh.write(url+mlink+"\n")
						#self.get_links(url+mlink)
						#mlink=""								
			elif mlink.startswith("#"):
				#print "SKIPPED"
				continue
			elif mlink.startswith(("http","https")):
				#print link
				if mlink not in self.urls:
					#print "URL:",mlink
					self.urls.append(mlink)
					##self.fh.write(mlink+"\n")
					#self.get_links(mlink)
					#link=""
			else:
				#print "SKIPPED"
				continue
		return	self.urls

if __name__=="__main__":
	ob=crawl_web()
	url_full=[]
	url='http://www.msn.com'
	ob.get_links(url)
	for url in ob.urls:
		print url
			
		
