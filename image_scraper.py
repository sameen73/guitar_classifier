#Getting the packages
#Used conda environment called env1, put up requirements.txt soon
#Figure out how to scrape the links off the HTML of the results
import requests 
from bs4 import BeautifulSoup
import os 

#Creating a new directory to deposit all stratocaster image files
strat_path = "./stratocaster_images"
if not os.path.exists(strat_path):
    os.makedirs(strat_path)

#Pulling page content 
URL = r'https://www.guitarcenter.com/Used/?Ntt=fender%20stratocaster&Ns=r' 
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#Getting the main parts of the page into results
results = soup.find_all("li", {'class':'product-container'})

#Empty list to store image links
imagelinks = []

#Extract and collect all image links
for result in results:
    image_info = result.find('img')
    imagelinks.append(image_info.attrs['data-original'])

#Downloading images via link 
for i, imagelink in enumerate(imagelinks):
    response = requests.get(imagelink)
    
    #Saving image with name as a .jpg file
    imagename = strat_path + '/' + 'strat' + str(i+1) + '.jpg'
    with open(imagename, 'wb') as file:
        file.write(response.content)
