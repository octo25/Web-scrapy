from urllib.request import urlopen 
from bs4 import BeautifulSoup
import csv

html = urlopen('http://markebisufuturistics.com/accounts/login/?next=/')
bs = BeautifulSoup(html, 'html.parser')

csvFile = open('Mark.csv', 'w')
writer = csv.writer(csvFile)

tbody = bs('span', {'cdir':'ltr'})[0].find_all('b')

for row in tbody:
	cols = row.findChildren(recursive=False)
	cols = [ele.text.strip() for ele in cols]
	writer.writerow(cols)
	print(cols)
	
   
	












