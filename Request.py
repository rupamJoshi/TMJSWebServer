import http.cookies as Cookie
class Request:
 def __init__(self,baseHttp,queryString={},type="GET"):
  self.__queryString=queryString
  self.__type=type
  self.__baseHttp=baseHttp
 def getQueryString(self):
  return self.__queryString
 def setQueryString(self,queryString):
  self.__queryString=queryString
 def getAttributeValue(self,attribute):
  if attribute in self.__queryString:
   return self.__queryString[attribute][0]
   return None
 def setType(self,type):
  self.__type=type
 def getType(self):
  return self.__type
 def getCookie(self,name):
  if "Cookie" in self.__baseHttp.headers:
   c= Cookie.SimpleCookie(self.__baseHttp.headers["Cookie"])
   return c[name].value
  return None

