import os
import json
class WebApplication:
	def __init__(self,homepage,files,pyMapping):
		self.__homepage=homepage
		self.__files=files
		self.__pyMapping=mapping

	def setHomePage(self,homepage):
		self.__homepage=homepage

	def getHomePage(self):
		return self.__homepage

	def setFiles(self,files):
		self.__files=files

	def getFiles(self):
		return self.__files

	def setPyMapping(self,pyMapping):
		self.__pyMapping=pyMapping

	def getPyMapping(self):
		return self.__pyMapping

file=open("server.conf","r+")
data=json.load(file)
contextNames=os.listdir('apps')
siteNames={}
print("hello")
for contextName in contextNames:	
	homepage=""
	files=[]
	pyMapping=[]
	for root,dirs,fs in os.walk('./apps/'+contextName):
		
		#print("Root ",root)
		#print("Directories ",dirs)
		#print("Files ",fs)
		#print("-----------------------------------------------")
		print("length ",len(fs))
		if len(fs) !=0:
			print(root.find("/private"))
			if root.find("/private")==-1:
				print("yahi yahi ",root)
				files=files+fs
		xyz="apps/"+contextName+"/private"
		if xyz in root and "app.conf" in fs:
			print(" hann site folder")
			file=open(xyz+"/app.conf","r+")
			appJsonData=json.load(file)
			homepage=appJsonData["homepage"]
			pyMapping=appJsonData["mapping"]
	print(files)
	#webApplication=webApplication(homepage,files,pyMapping)
			
