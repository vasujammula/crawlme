#!/usr/bin/python
import urllib
import lxml.html
import httplib2
import time
import subprocess
class crawl_web:
	
	def __init__(self,urls=[],filename="urls.txt"):
		self.urls=urls	
		self.t_urls=[]
		self.fh=open(filename,"w+")
		self.close_after=20
		self.lf=open("crawler_exec.log","a+")	


	
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
	def open_link(self,url,browser="firefox"):
		#print "OPENING URL:",url
		self.lf.write("INFO:OPENING URL"+url+"\n")
		try:
			try:
				subprocess.Popen(["ps -ef | grep "+browser+" |grep defunct | grep -v grep | cut -b8-20 | xargs kill -9"])
			except Exception as e1:
				#print "\nWhile Closing browser got exception plz ignore "
				self.lf.write("DEBUG:While Closing browser got exception plz ignore"+"\n")
			browser_in=subprocess.Popen([browser,url],stdout=None, stderr=None)
			time.sleep(self.close_after)
			browser_in.terminate()
			self.lf.write("URL OPENED SUCCESSFULLY....:"+url+"STATUS CODE:"+str(urllib.urlopen(url).getcode())+"\n")
		except Exception as e2:
			print "Exception while accessing url",url,e2.message
			self.lf.write("DEBUG:Exception while accessing url"+"\n")	
			
if __name__=="__main__":
	ob=crawl_web()
	url_full=[]
	url='http://www.msn.com'
	ob.get_links(url)
	for url in ob.urls:
		#print url
		ob.open_link(url,"firefox")	
