

from bs4 import BeautifulSoup
import requests

url='http://www.shopping.com/products?'

query1={
	'KW' :'car-seats'
}

query2={
	'pg' : '2',
	'KW' : 'car-seats'
}

class Fetch:
	def __init__(self,param):
		self.param=param
		self.response=requests.get(url,params=param)
		self.soup=BeautifulSoup(self.response.content,'html.parser');
	def Query1(self):
		print self.soup.find_all("span",{"class":"numTotalResults"})[0].contents[0]
	
	def Query2(self):
		countProducts=0;
		g_data=self.soup.find_all("div", {"class":"gridItemBtm"});
		for item in g_data:
			try:
				print  item.find_all("a",{"class":"productName"})[0].contents[1]['title']
				countProducts+=1
			except:
				pass
		print "Total Products: ",countProducts

	
if __name__=='__main__':

	try :
		q1=Fetch(query1)
		q1.Query1()

		q2=Fetch(query2)
		q2.Query2()
	except:
		pass

