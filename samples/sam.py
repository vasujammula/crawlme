#!/usr/bin/python
import urllib
import lxml.html
import time
import subprocess
import sys
import thread
class crawl_web:
	
	def __init__(self,urls=[],filename="urls.txt"):
		self.urls=urls	
		self.t_urls=[]
		self.fh=open(filename,"w+")
		self.close_after=25
		self.lf=open("crawler_exec.log","a+")	
                self.platform=sys.platform
                if(self.platform=="linux"):
                    self.browser="firefox"
                elif(self.platform=="win32"):
                    self.browser="C:\Program Files (x86)\Mozilla Firefox\\firefox.exe"
	        else:
                    self.browser="firefox"
	def get_links(self,url):
		connection = urllib.urlopen(url)
		dom =  lxml.html.fromstring(connection.read())

		for mlink in dom.xpath('//a/@href'):
			if mlink.startswith("/"):
				if mlink.startswith("/#"):
					continue
				elif mlink.startswith("/#"):
					continue
				else:
					if url+mlink not in self.urls:
						self.urls.append(url+mlink)
			elif mlink.startswith("#"):
				continue
			elif mlink.startswith(("http","https")):
				if mlink not in self.urls:
					self.urls.append(mlink)
			else:
				continue
		for url in self.urls:
                        ob.open_link(url,self.browser)
		#return	self.urls
	def open_link(self,url,browser="firefox"):
                if(self.platform=="win32" or self.platform=="linux2"):
                    self.lf.write("INFO:OPENING URL"+url+"\n")
		    try:

                        try:
                            #This works for linux platform to close all instances of browser running Need to add support for win32
                            subprocess.Popen(["ps -ef | grep "+browser+" |grep defunct | grep -v grep | cut -b8-20 | xargs kill -9"])
			except Exception as e1:
				self.lf.write("DEBUG:While Closing browser got exception plz ignore"+"\n")
			browser_in=subprocess.Popen([browser,url],stdout=None, stderr=None)
			time.sleep(self.close_after)
			browser_in.terminate()
			self.lf.write("URL OPENED SUCCESSFULLY....:"+url+"STATUS CODE:"+str(urllib.urlopen(url).getcode())+"\n")
		    except Exception as e2:
			self.lf.write("DEBUG:Exception while accessing url"+e2.message+"\n")	
                else:
                     self.lf.write("ERROR:THIS PROGRAM WONT WORK WITH THIS PLATFORM \n")
		    
if __name__=="__main__":
	ob=crawl_web()
	url_full=[]
	fh=open(filename,"w+")
	for link in fh:
	#url='http://www.msn.com'
		thread.start_new_thread(ob.get_links,(url))
	#for url in ob.urls:
        #       ob.open_link(url,ob.browser)
