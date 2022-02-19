#Import packages
from bs4 import BeautifulSoup
import requests

#Set the url
url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.xml"

def getinfo():
  #Get the webpage
  page = requests.get(url)

  #Parse the page
  if page.status_code == 200:    
    #Parse the page to variable soup
    soup = BeautifulSoup(page.text, "html.parser")  

    #Create array of required informations
    info = ["tanggal", "jam", "datetime", "lintang", "bujur", "magnitude", 
            "kedalaman", "wilayah", "potensi"]

    #Get the information from the parsed page
    print("Telah terjadi gempa dengan keterangan sebagai berikut: ")
    for word in info:
      data = soup.find(word)
      data = data.text
      print(word.capitalize(), ":", data.capitalize())

  else:
    print("The source can't be accessed.")

getinfo()