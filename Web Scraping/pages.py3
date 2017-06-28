##### Counting pages of beaches
##### May not be needed??? Weird 


##### Counting pages in reviews
import requests
page = requests.get("https://www.tripadvisor.com/Attraction_Review-g644260-d2233143-Reviews-Cala_Mariolu-Baunei_Province_of_Ogliastra_Sardinia.html")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
rating = soup.find(id= "taplc_location_detail_header_attractions_0")
review = rating.find_all(class_="rs rating")
reviews = review[0]
numbers = reviews.find(class_="more").get_text()
# print(numbers)
count = numbers.partition(" ")[0]
print(count)
