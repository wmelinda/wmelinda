#####
import time
starttime1 = time.time()

#import urllib2
from urllib2 import urlopen
from bs4 import BeautifulSoup

url = 'https://www.tripadvisor.com/Attractions-g187768-Activities-c61-t52-Italy.html'

#conn = urllib2.urlopen(url)
conn = urlopen(url)
html = conn.read()

soup = BeautifulSoup(html, "html.parser")
links = soup.find_all('a')

weblinks = []
for tag in links:
  link = tag.get('href',None)
  if (link and ('Attraction_Review' in link) and ('#REVIEWS' not in link)): 
    print (link)
    weblinks.append(link)

weblinks1 = []
for link in weblinks:
	if link not in weblinks1:
		weblinks1.append(link)

file = open ('webs', 'w')
for link in weblinks1:
               file.write(str(link))
               file.write("\n")
file.close()

##### Results: file title 'webs' with all the links to all the beaches tripadvisor has in Italy 

import requests
import webbrowser, requests, bs4, time
import re 

# prepare searchwords
# get the key words from the file named "keywords"
searchwords = []
keyfile = open("keywords", "r")
for line in keyfile:
  print(line)
  keyword = line.rstrip()
  searchwords.append(keyword)
keyfile.close() 


##### Open webpages to find # of review for each beach 
for link in weblinks1:
  starttime2 = time.time()
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
##### Collect the other info we need to get the reviews
  matchcount = 3
  part1 = url.partition("Reviews-")[0] + "or"
# e.g. part1 = 'https://www.tripadvisor.com/Attraction_Review-g150807-d152697-Reviews-or'
  part2 = url.split("Reviews",1)[1]
# e.g. part2 = '-Playa_Langosta-Cancun_Yucatan_Peninsula.html#REVIEWS'
  m = re.search('Reviews-(.+?).html', url)
  if m: 
    beachname = m.group(1)
# beachname = 'Playa_Langosta-Cancun_Yucatan_Peninsula'
#check to see if there is a file already made 
  import os.path
  if os.path.isfile("/" + beachname + ".html"): 
    continue
  else: 
    pass
# define result dictionary
  results ={}
# 
# every page has 10 reviews. calculate number of pages to look at
  pagenums = int(reviewnum / 10) 
  maxN = 200
  pagenum = max(maxN, pagenums)
  print("There are ", pagenum, " pages to search and there are total ", reviewnum, " reviews")
  for swd in searchwords:
    results[swd] = []
##### Now we start collecting reviews 
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
        # define the regular expression for search, i.e, put the search word in a word boundary
        my_regex = r"\b" + swd + r"\b"
 
        text = items[z].getText()
 
        s = re.search(my_regex, text, re.IGNORECASE)
        if (s):
        # found the match word
          matchword = text[s.start():s.end()]
          print ('\nfound match word:', matchword)
 
          # insert color tag for the matchword
          newtext = text[:s.start()] + '<font color="red">' + matchword + '</font>' + text[s.end():]
          sentence = str(newtext.encode('ascii', 'ignore'));
 
          # insert paragraph tag
          clean_sentence = '<p>' + sentence.replace("\\n", " ") + "</p>"
          results[swd].append(clean_sentence)

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

    # insert html definition
    file.write('</body>\n')
    file.write('</html>\n')
    file.close()

endtime1 = time.time()
difftime1 = endtime1 - starttime1
print ("used time :", difftime1, " seconds")
