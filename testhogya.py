import socket
import sys
import os
import subprocess
from subprocess import Popen,PIPE
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
# GET
	def do_GET(self):
		print("Request aayi")
		print(self.path)
		urlPath=''
		if self.path=='/':
			urlPath='./default/index.html'
			print("default wale iff me agya")
			#file=open('./default/index.html','r+')
			#self.wfile.write(file.read().encode())
		else:
			path=self.path
			path=path.split("/")
			if len(path)==2:
				print('./apps/'+path[1]+'/index.html')
				if os.path.isfile('./apps/'+path[1]+'/index.html'):	
					print('index.html found')
					#indexFile=open('./apps/'+path[1]+'/index.html')
					urlPath='./apps/'+path[1]+'/index.html'
					#self.wfile.write(indexFile.read().encode())
				else:
					print('index.html not found')
					if os.path.isfile('./apps/'+path[1]+'/index.htm'):
						print('index.htm found')
					#	indexDotHtmFile=open('./apps/'+path[1]+'/index.htm')
					#	self.wfile.write(indexDotHtmFile.read().encode())
						urlPath='./apps/'+path[1]+'/index.htm'

					else:
						print('index.htm not found')
							
						if os.path.isfile('./apps/'+path[1]+'/index.py'):
							print("bhagwan ke ly chal ja")
							urlPath='./apps/'+path[1]+'/index.py'
			else:
				if path[2]=='private':
					print("Kuch nahi ho sakta")
					self.wfile.write(bytes("404 NOT FOUND","utf-8"))
				else:
				 	urlPath='./apps'+self.path
			
		f=open(urlPath,'rb')
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(f.read())
		f.close()
		print(urlPath)
		return

def run():	
	print('starting server...')
	# Server settings
	# Choose port 8080, for port 80, which is normally used for a 		http server, you need root access
	server_address = ('192.168.1.175', 5050)
	httpd = HTTPServer(server_address,testHTTPServer_RequestHandler)
#	print(testHTTPServer_RequestHandler)
	print('running server...')
	httpd.serve_forever()

run()
	
