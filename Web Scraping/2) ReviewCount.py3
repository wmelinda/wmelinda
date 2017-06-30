#Second segment of the code! 
#This code counts the number of pages (of reviews). We need this number in order to tell the program how many pages it should skim through. 

#Setup
import requests
from bs4 import BeautifulSoup

#This is the URL we are using as an example 
page = requests.get("https://www.tripadvisor.com/Attraction_Review-g644260-d2233143-Reviews-Cala_Mariolu-Baunei_Province_of_Ogliastra_Sardinia.html")

#This is some handy code I was able to pull together after some research online! 
#What it does, is look through the HTML of the code 
#The HTML of the TripAdvisor link with the review number can be found by using 'Inspect'
#In addition, highlighting over the HTML code colors the sections the code is influencing 
#From the program, we target specific sections of the HTML until it zeroes in on the section we want - the number of reviews on the specific beach 

#Setting up HTML parser
soup = BeautifulSoup(page.content, 'html.parser')

#Finding the target div id 
rating = soup.find(id= "taplc_location_detail_header_attractions_0")

#Finding the target div class
review = rating.find_all(class_="rs rating")

#Extract first element 
reviews = review[0]

#Finding the target class to find where the number is 
numbers = reviews.find(class_="more").get_text()

#If you ask to 'print numbers', the result will be '1,408 Reviews' 

#Remove the extra text after the number
count = numbers.partition(" ")[0]

#Print the number (to check the code) 
print(count)
