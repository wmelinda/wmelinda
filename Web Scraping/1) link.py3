#This is the first part of my code! 
#I was looking to 



#### Gathering links from webpage about beaches --- need to get loop for the page !!! 
import urllib2
from bs4 import BeautifulSoup

url = 'https://www.tripadvisor.com/Attraction_Review-g652016-d3211983-Reviews-La_Cinta-San_Teodoro_Province_of_Olbia_Tempio_Sardinia.html'

conn = urllib2.urlopen(url)
html = conn.read()

soup = BeautifulSoup(html, "lxml")
links = soup.find_all('a')

weblinks = []
for tag in links:
    link = tag.get('href',None)
    if link is not None:
    	if 'Attraction_Review' in link: 
    		if '#REVIEWS' not in link: 
    			print link
    			weblinks.append(link)

weblinks1 = []
for link in weblinks:
	if link not in weblinks1:
		weblinks1.append(link)

file = open ('webs', 'w')
for link in weblinks1:
               file.write("\n")
               file.write(str(link))
file.close()
