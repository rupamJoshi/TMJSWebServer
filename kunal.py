import socket
import sys
import os
import subprocess
from subprocess import Popen,PIPE
from http.server import BaseHTTPRequestHandler, HTTPServer
from mimetypes import MimeTypes
import tmserver
from pprint import pprint
from urllib.parse import *
import importlib
import Request,Response
# HTTPRequestHandler class
#global siteNames
import http.cookies as Cookie
class TestHTTPServerRequestHandler(BaseHTTPRequestHandler):
 def sendCookie(self):
  c=Cookie.SimpleCookie()
  c['name']='Bablu'
  c['sex']='M'
  self.send_header('Set-Cookie',c.output(header=''))
  self.end_headers()
  self.wfile.write(bytes("<!doctype html><html><head><meta charset='utf-8'></head><body><a href='/kunal'>Cookie</a>"))
 def do_GET(self):
  print("************************************************")
  if self.path=='/kunal':
   if "Cookie" in self.headers:
      c = Cookie.SimpleCookie(self.headers["Cookie"])
      print(c['name'].value)   
  c=Cookie.SimpleCookie()
  c['name']='Bablu'
  c['sex']='M'
  self.send_response(200)
  self.send_header('Set-Cookie',c.output(header=''))
  self.send_header('Content-type','text/html')
  self.end_headers()
  self.wfile.write(bytes("<!doctype html><html lang='en'><head><meta charset='utf-8'></head><body><a href='/kunal'>Cool</a>",'utf-8'))
  return
  mime=MimeTypes()
  mimeType=mime.guess_type(self.path)
  print("Request aayi")
  urlParseData=urlparse(self.path) 
  urlPath=urlParseData[2]
  query=urlParseData[4]
  print(query)
  if query!='':
   query=parse_qs(query)
   print(query)
   print("name ",query["nm"][0])
  newPath=''
  if urlPath=='/' or urlPath=='/favicon.ico':
   newPath='./default/index.html'
   print("default wale iff me agya")
  else:
   path=urlPath
   path=path.split("/")
   print(path[1])
   if path[1] in siteNames :
    if len(path)==2:
     print('./apps/'+path[1]+'/index.html')
     if os.path.isfile('./apps/'+path[1]+'/index.html'):	
      print('index.html found')
     # urlPath='./apps/'+path[1]+'/index.html'
      print('index.html not found')
      if os.path.isfile('./apps/'+path[1]+'/index.htm'):
       print('index.htm found')
       #urlPath='./apps/'+path[1]+'/index.htm'
       newPath=urlPath+'/index.html'
      else:
       print('index.htm not found')
       if os.path.isfile('./apps/'+path[1]+'/index.py'):
        print("index.py found")
       # urlPath='./apps/'+path[1]+'/index.py'
        newPath=urlPath+'/index.html'
       else:
        self.send_error(404,"home page not found")
        return
     self.send_response(301)
     self.send_header('Location',newPath) 
     self.end_headers()
     return
    else:
     if path[2]=='private':
      print("Kuch nahi ho sakta")
      self.wfile.write(bytes("404 NOT FOUND","utf-8"))
     else:
      a=self.path.find("/")
      print("index ",a)
      abcd=urlPath[urlPath.find("/",a+1):]
      print("aaaaabcdcdbvava",abcd)
      mapping=siteNames[path[1]].getMapping()
      if abcd in mapping:
        print("py exitssssssssssssssssss karti h")
        a=mapping[abcd].rfind(".")
        if a!=-1:
         fileName=mapping[abcd][a+1:]
         print(fileName)
         packageName=mapping[abcd][:a]
         ieiprint(packageName)
         finalpath='apps.'+path[1]+".private."+packageName+"."+fileName
         moduleName=__import__(finalpath,fromlist=fileName)
         request=Request(query,self.command)
         response=Response(self.wfile,'text/html')
         moduleName.process(request,response)
        else:
         finalpath='apps.'+path[1]+".private."+mapping[abcd]
         moduleName=__import__(finalpath,fromlist=mapping[abcd])
         request=Request(query,self.command)
         response=Response(self.wfile,'text/html')
         moduleName.process() 
      else:
       newPath='./apps'+urlPath#self.path[self.path.find("/"):]
       mimeType=mime.guess_type(newPath)	
       
   else:
    self.send_error(404,'%s Not Found' %(path[1]))
  try:
   #mimeType=mime.guess_type(newPath)
   print(mimeType)
   print(newPath) 
   f=open(newPath,'rb')
   self.send_response(200)
   self.send_header('Content-type',mimeType)
   self.end_headers()
   self.wfile.write(f.read())
   f.close()
  except IOError:
   print("File does not exist");
   self.send_error(404,'File Not Found: %s' % urlPath)
 # print(urlPath)
  return
def run():	
 global siteNames
 siteNames=tmserver.loadSites()
 
 configuration=tmserver.loadConfiguration()
 print('starting server...')
 server_address = (configuration["ip"],5051 )
 httpd = HTTPServer(server_address,TestHTTPServerRequestHandler)
 print('running server...')
 httpd.serve_forever()

 print("*Fhsahfahf******FHDHF*DHFHDH*D*D*HDF*DFH*")
run()
	
