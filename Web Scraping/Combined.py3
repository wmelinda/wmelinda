#Combined code that does all of the processes listed in parts 1 - 4  + some extra bits as well. 
#Feel free to look at those segments if you would like some more details about the code! 

#Setup & Time start 
import time, math
starttime1 = time.time()

#Setup 
from urllib2 import urlopen
from bs4 import BeautifulSoup
import webbrowser, requests, bs4
import re 

#URL that has beaches within Italy 
url = 'https://www.tripadvisor.com/Attractions-g187768-Activities-c61-t52-Italy.html'

########## Part 1) LinkPull

#Open the URL and read the HTML 
conn = urlopen(url)
html = conn.read()

#Find the links within the HTML
soup = BeautifulSoup(html, "html.parser")
links = soup.find_all('a')

#Create a list named 'weblinks' that collects the links of the beaches in Italy 
weblinks = []
for tag in links:
  link = tag.get('href',None)
  if (link and ('Attraction_Review' in link) and ('#REVIEWS' not in link)): 
    print (link)
    weblinks.append(link)

#Create a list named 'weblinks1' that removes duplicates of links 
weblinks1 = []
for link in weblinks:
	if link not in weblinks1:
		weblinks1.append(link)

#Create a file named 'webs' and write all the links within the file 
file = open ('webs', 'w')
for link in weblinks1:
               file.write(str(link))
               file.write("\n")
file.close()

########### Results: file title 'webs' with all the links to all the beaches tripadvisor has in Italy 

#Prepare keywords for search
#Get the key words from the file named "keywords"
#Create a list named 'searchwords' that contains the keywords 
searchwords = []
keyfile = open("keywords", "r")
for line in keyfile:
  print(line)
  keyword = line.rstrip()
  searchwords.append(keyword)
keyfile.close() 

########## Part 2) ReviewCount 

#Segment weblinks to find the number of reviews on each beach 
for link in weblinks1:
  url = "https://www.tripadvisor.com" + str(link)
  print(url)
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  header = soup.find(id= "taplc_location_detail_header_attractions_0")
  rating = header.find(class_= "rating_and_popularity")
  review = rating.find(class_="rs rating")
  numbers = review.find(class_="more").get_text()
  count = numbers.partition(" ")[0]
  reviewnum = int(count.replace(',',''))
	
########## Part 3) KeywordSearch 
	
#Matchcount is the maximum number of reviews you want to record for each keyword 
  matchcount = 3

#Partition URLs to later loop through pages of reviews 
  part1 = url.partition("Reviews-")[0] + "or"
  part2 = url.split("Reviews",1)[1]

#Record beach name to use as file name later 
  m = re.search('Reviews-(.+?).html', url)
  if m: 
    beachname = m.group(1)

########## Part 4) FileCheck 

#Check to see if there is a file already made, skips over beach if file with the same name is already made 
  import os.path
  if os.path.isfile("/" + beachname + ".html"): 
    continue
  else: 
    pass

#Create results dictionary 
  results ={}

#Every page has 10 reviews. Calculate the number of pages to look at and loop through 
  pagenums = int(math.ceil(reviewnum / 10))
  maxN = 200
  pagenum = max(maxN, pagenums)
  print("There are ", pagenum, " pages to search and there are total ", reviewnum, " reviews")

#For each keyword, scan through the reviews and each page of reviews 
  for swd in searchwords:
    results[swd] = []
  for x in range(pagenum):
    print ("########## In page ", x, "\n")
    y = x * 10
    if (y == 0):
      link = url
    else:
      link = part1 + str(y) + part2
    res=requests.get(link) 
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    items= soup.select('p')

    for z in range(len(items)):
      for swd in searchwords:
        if (len(results[swd]) == matchcount):
          continue
 
#Define what pattern to search for (the search word) - put the search word in a word boundary ('\b')
#The boundary prevents the word from recognizing words with the keyword within it (e.g. 'bus' and 'business')
        my_regex = r"\b" + swd + r"\b"
 
        text = items[z].getText()
 
#This ignores the case of the words (lowercase and uppercase) 
        s = re.search(my_regex, text, re.IGNORECASE)

#If word matches, print that the matched word has been found 
	if (s):
          matchword = text[s.start():s.end()]
          print ('\nfound match word:', matchword)
 
#Highlight the keyword in red 
          newtext = text[:s.start()] + '<font color="red">' + matchword + '</font>' + text[s.end():]
          sentence = str(newtext.encode('ascii', 'ignore'));
 
#Append sentence to results list
          clean_sentence = '<p>' + sentence.replace("\\n", " ") + "</p>"
          results[swd].append(clean_sentence)

#Create a file with the beach name as a title 
    filename = beachname + '.html'
    file = open (filename, 'w')
    file.write('<!DOCTYPE html>\n')
    file.write('<html>\n')
    file.write('<body>\n\n')
    for swd in searchwords:
      file.write('\n\n\n<h2>Matching results of <font color="red">')
      file.write(str(swd))
      file.write("</font> </h2>\n\n")
      file.write(str("\n\n".join(results[swd])))

#Set headers and body definitions for the HTML code
    file.write('</body>\n')
    file.write('</html>\n')
    file.close()

#End time for running code
endtime1 = time.time()
difftime1 = endtime1 - starttime1
print ("used time :", difftime1, " seconds")
