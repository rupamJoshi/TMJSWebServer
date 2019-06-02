import os
import json
from pprint import pprint
class WebApplication:
	def __init__(self,homepage="",mapping=None):
		self.__homepage=homepage
		self.__mapping=mapping

	def setHomePage(self,homepage):
		self.__homepage=homepage

	def getHomePage(self):
		return self.__homepage

	def setMapping(self,mapping):
		self.__mapping=mapping

	def getMapping(self):
		return self.__mapping

def loadConfiguration():
	serverJsonData={}
	try:
		file=open("server.conf","r+")
		try:
			serverJsonData=json.load(file)
		except:
			print("server.conf json is incorrect")
	except:
		print("server.conf is Not Found")
	return serverJsonData

def loadSites():
	siteNames={}
	contextNames=os.listdir('apps')
	for contextName in contextNames:	
		webApplication= WebApplication()
		print("------------------")
		print(contextName)
		for root,dirs,fs in os.walk('./apps/'+contextName):
			xyz="apps/"+contextName+"/private"
			if xyz in root :
       # sys.path.insert(0,"./apps/"+contextName+"/private")
				if "app.conf" in fs:
					try:
						file=open(xyz+"/app.conf","r+")
						try:
							appJsonData=json.load(file)
							if "homepage" in appJsonData:
								webApplication.setHomePage(appJsonData["homepage"])
							if "mapping" in appJsonData:
								webApplication.setMapping(appJsonData["mapping"])
						except:
							print("app.conf is incorrect")
					except IOError:
						print("File app.conf not found in private")	
				else:
						print("File app.conf not found in private")	
		siteNames[contextName]=webApplication
		print("------------------------------------")
	return siteNames

