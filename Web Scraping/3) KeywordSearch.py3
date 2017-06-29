#The third segment of code searches for reviews that specifically mention previously set keywords 
#This is honestly where the bulk of the code is haha 
#Got some help from my amazing mother to help code all the loops !! 
#They keywords are saved in a file titled 'keywords', which each new line having one keyword 

#Setup
import webbrowser, requests, bs4, time
import re 

#Because this code takes a while to run, I wanted to keep track of how long it took for my code to run 
#This code starts the clock to time how long it takes for your program to complete 
starttime = time.time()
 
#This is the URL used as an example 
reviewhttp = 'https://www.tripadvisor.com/Attraction_Review-g652016-d3211983-Reviews-La_Cinta-San_Teodoro_Province_of_Olbia_Tempio_Sardinia.html'
 
#Looked up the number of reviews on the website and physically inserted it myself
reviewnum = 201
 
#Wanted to limit the number of reviews that were returned, so added this number to limit the number of reviews per keyword that is found
matchcount = 3

#For each new link on TripAdvisor, there is one segment in the middle of the URL that changes 
#To go to page 2, TripAdvisor ads a multiple of 10 after 'or' and a dash ('-') as well
#e.g. https://www.tripadvisor.com/Attraction_Review-g644260-d2233143-Reviews-Cala_Mariolu-Baunei_Province_of_Ogliastra_Sardinia.html
# ->: https://www.tripadvisor.com/Attraction_Review-g644260-d2233143-Reviews-or10-Cala_Mariolu-Baunei_Province_of_Ogliastra_Sardinia.html

#So, to have the code cycle through the pages, there needs to be a loop that continues to run through these different links/pages
#Need to partition the code into two sections so that they can be reconstructed in the future to create all the page links 
part1 = reviewhttp.partition("Reviews-")[0] + "or"
# part1 = 'https://www.tripadvisor.com/Attraction_Review-g644260-d2233143-Reviews-or'
part2 = reviewhttp.split("Reviews",1)[1]
# part2 = 'Cala_Mariolu-Baunei_Province_of_Ogliastra_Sardinia.html'

#To name the file the name of the beach, I also segmented the URL to pick out the beach name 
m = re.search('Reviews-(.+?).html', reviewhttp)
if m: 
     beachname = m.group(1)
# beachname = 'Cala_Mariolu-Baunei_Province_of_Ogliastra_Sardinia'

#Define result dictionary (set it up) 
results ={}
 
#Create a list for words to search for ('searchwords') 
#Get the key words from the file named "keywords"
searchwords = []
keyfile = open("keywords", "r")
for line in keyfile:
               print(line)
               keyword = line.rstrip()
               searchwords.append(keyword)
keyfile.close()
 
#Because every page has 10 reviews, we find the number of pages by dividing the number of reviews by 10 and rounding to the nearest integer
page = int(math.ceil(reviewnum / 10))

#Print this statement to make sure the code is running and that the numbers or okay 
print("There are ", page, " pages to search and there are total ", reviewnum, " reviews")
 
#Open the review page to make sure it's correct
#[I don't have this in the combined code. That would be terrible.] 
webbrowser.open(reviewhttp)


#For each word in the searchwords list (aka the keywords), insert them in the results directory that was previously created. 
for swd in searchwords:
               results[swd] = []
 
 
 
#FIRST LOOP: for each page:

# Print a statement that states which page you find keywords in, or print that you have looked through the page 
for x in range(page):
               print ("########## In page ", x, "\n")
               y = x * 10
   
   #This section of code is to assist with creating the page links 
               if (y == 0):
                              link = reviewhttp
               else:
                              link = part1 + str(y) + part2
    
    #This section of code calls up the link and parses out the paragraph HTML sections (text of reviews !)            
               res=requests.get(link)
               soup = bs4.BeautifulSoup(res.text, "html.parser")
               items= soup.select('p')
 
    
    
    #SECOND LOOP: For each word in the texts we've collected: 
               for z in range(len(items)):
      
      
      
      #THIRD LOOP: For each keyword in the searchword list: 
                              for swd in searchwords:
        #IF: number of results of the searchword = number of max reviews we want to collect - 
           #Move onto the next word 
        #ELSE: continue through the code 
        #Searc
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
