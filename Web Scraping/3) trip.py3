
import webbrowser, requests, bs4, time
 
# Print current time
starttime = time.time()
 
# specify the review link
reviewhttp = 'https://www.tripadvisor.com/Attraction_Review-g652016-d3211983-Reviews-La_Cinta-San_Teodoro_Province_of_Olbia_Tempio_Sardinia.html'
 
# specify number of reviews
reviewnum = 201
 
# specify how many matches needed
matchcount = 3
 
part1 = reviewhttp.partition("Reviews-")[0] + "or"
# part1 = 'https://www.tripadvisor.com/Attraction_Review-g150807-d152697-Reviews-or'
part2 = reviewhttp.split("Reviews",1)[1]
# part2 = '-Playa_Langosta-Cancun_Yucatan_Peninsula.html#REVIEWS'
import re 
m = re.search('Reviews-(.+?).html', reviewhttp)
if m: 
     beachname = m.group(1)
# beachname = 'Playa_Langosta-Cancun_Yucatan_Peninsula'

# define result dictionary
results ={}
 
# get the key words from the file named "keywords"
searchwords = []
keyfile = open("keywords", "r")
for line in keyfile:
               print(line)
               keyword = line.rstrip()
               searchwords.append(keyword)
keyfile.close()
 
 
# every page has 10 reviews. calculate number of pages to look at
page = int(reviewnum / 10)
 
print("There are ", page, " pages to search and there are total ", reviewnum, " reviews")
 
# open the review page to make sure it's correct
webbrowser.open(reviewhttp)
 
for swd in searchwords:
               results[swd] = []
 
# go through each page
for x in range(page):
               print ("########## In page ", x, "\n")
               y = x * 10
               if (y == 0):
                              link = reviewhttp
               else:
                              link = part1 + str(y) + part2
              
               res=requests.get(link)
               soup = bs4.BeautifulSoup(res.text, "html.parser")
               items= soup.select('p')
 
               for z in range(len(items)):
                              for swd in searchwords:
                                             if (len(results[swd]) == matchcount):
                                                            continue
                                             wd = ' ' + swd
                                             wd1 = ' ' + swd.lower()
                                             if (len(wd1) < 5):
                                                            wd1 = wd1 + ' '
                                             text = items[z].getText()
                                             if ((wd in text) or (wd1 in text)):
                                                            print ('\nfound match word:', wd, ' or ', wd1, '\n')
                                                            print (items[z].getText())
                                                            sentence = str(text.encode('ascii', 'ignore'));
                                                            clean_sentence = sentence.replace("\\n", " ")
                                                            results[swd].append(clean_sentence)
 
def write_red(file, str_):
     file.write('<p style="color:#ff0000">%s</p>' % str_)

file = open (beachname, 'w')
for swd in searchwords:
               file.write("\n")
               file.write("\n")
               file.write("\n\n#####<<<<< Matching results of ")
               file.write(str(swd))
               file.write(" >>>>>#####\n\n")
               file.write(str("\n\n".join(results[swd])))
file.close()
 
# Print current time
endtime = time.time()
difftime = endtime - starttime
print ("used time :", difftime, " seconds")
