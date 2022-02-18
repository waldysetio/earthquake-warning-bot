#Import packages
from bs4 import BeautifulSoup
import requests

#Set the url
url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.xml"

def getinfo():
  #Get the webpage
  page = requests.get(url)

  #Parse the page
  if page.status_code is 200:    
    #Parse the page to variable soup
    soup = BeautifulSoup(page.text, "xml")  

    #Create array of required informations
    info = ["Tanggal", "Jam", "DateTime", "Lintang", "Bujur", "Magnitude", 
            "Kedalaman", "Wilayah", "Potensi"]

    #Get the information from the parsed page
    print("Telah terjadi gempa dengan keterangan sebagai berikut: ")
    for word in info:
      data = soup.find(word)
      print(word, ":", data.text)

  else:
    print("The source can't be accessed.")

getinfo()