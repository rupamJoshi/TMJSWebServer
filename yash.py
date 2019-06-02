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
import Request
from Request import Request
import Response
from Response import Response
# HTTPRequestHandler class
#global siteNames
class TestHTTPServerRequestHandler(BaseHTTPRequestHandler):
 def do_GET(self):
  print("************************************************")  
  mime=MimeTypes()
  mimeType=mime.guess_type(self.path)
  print("Request aayi")
  urlParseData=urlparse(self.path) 
  print("URLPARSEDATA****  ",urlParseData)
  urlPath=urlParseData[2]
  query=urlParseData[4]
  print("QUERY *****",query)
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
      newPath=urlPath+'/index.html'
     else:
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
         print(packageName)
         finalpath='apps.'+path[1]+".private."+packageName+"."+fileName
         moduleName=__import__(finalpath,fromlist=fileName)
         #request=Request
         self.send_response(200)
         request=Request(query)
         response=Response(self,self.wfile,'text/html')
         moduleName.process(request,response)
         #self.send_header('Content-type',response.getContentType())
         #self.end_headers()
         return
        else:
         finalpath='apps.'+path[1]+".private."+mapping[abcd]
         moduleName=__import__(finalpath,fromlist=mapping[abcd])
         self.send_response(200)
         request=Request(query)
         response=Response(self,self.wfile,'text/html')
         moduleName.process(request,response)
         #self.send_header('Content-type',response.getContentType())
         #self.end_headers()
         return 
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
 server_address = (configuration["ip"], configuration["port"])
 httpd = HTTPServer(server_address,TestHTTPServerRequestHandler)
 print('running server...')
 httpd.serve_forever()
run()
	
