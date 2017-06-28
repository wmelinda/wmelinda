#This is the first part of my code! 

#I was looking to pull all of the beach-related URLs from TripAdvisor. 
#I was thinking of including a loop for pages (e.g. the code would run through and collect links from different pages), but I found that all the beaches were listed on one page.

#Setup
import urllib2
from bs4 import BeautifulSoup

#URL to use 
url = 'https://www.tripadvisor.com/Attraction_Review-g652016-d3211983-Reviews-La_Cinta-San_Teodoro_Province_of_Olbia_Tempio_Sardinia.html'

#Open and read URL 
conn = urllib2.urlopen(url)
html = conn.read()

#Look through the HTML and find links on the page [generally known with 'ahref'] 
soup = BeautifulSoup(html, "lxml")
links = soup.find_all('a')

#Create new list titled 'weblinks'  
#This list sorts through the links of the page - selecting those that are reviews of attractions ('Attraction_Review') 
#This list also removes some of the duplicates of the same beach (link to beach page vs link to reviews of the beach - also on the beach page) 
#The links are then stored in the weblinks list 
weblinks = []
for tag in links:
    link = tag.get('href',None)
    if link is not None:
    	if 'Attraction_Review' in link: 
    		if '#REVIEWS' not in link: 
    			print link
    			weblinks.append(link)

#Create new list titled 'weblinks1' 
#This is the list of links with NO DUPLICATES - only add new links if the new links are not already in weblinks1
weblinks1 = []
for link in weblinks:
	if link not in weblinks1:
		weblinks1.append(link)
 
#Write all these links into a file, each on a new line 
#Save the file with the name 'webs' 
file = open ('webs', 'w')
for link in weblinks1:
               file.write("\n")
               file.write(str(link))
file.close()
