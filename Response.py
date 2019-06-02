import http.cookies as Cookie
class Response:
 def __init__(self,baseHttp,responseWriter=None,contentType='text/html'):
  self.__responseWriter=responseWriter
  self.__contentType=contentType
  self.__baseHttp=baseHttp
  self.__cookie=Cookie.SimpleCookie()
 def addCookie(self,name,value):
  self.__cookie[name]=value
 def write(self,str,type="utf-8"):
  self.__responseWriter.write(bytes(str,type))
 def setHeader(self,name,value):
  self.__baseHttp.send_header(name,value)
 def setContentType(self,contentType='text/html'):
  self.__contentType=contentType
  #self.__baseHttp.send_header('Set-Cookie',self.__cookie.output(header=''))
  self.__baseHttp.send_header('Content-type',contentType)
  #self.__baseHttp.send_header('Set-Cookie',self.__cookie.output(header=''))
  self.__baseHttp.end_headers()
 def getContentType(self):
  return self.__contentType
