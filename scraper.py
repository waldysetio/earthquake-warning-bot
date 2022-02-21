def getinfo():
  """Scrape BMKG website and return earthquake information"""

  #Import packages
  import requests
  from bs4 import BeautifulSoup

  #Set the url
  url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.xml"
  
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
    report = ""
    new_line = '\n'
    for word in info:
      data = soup.find(word)
      data = data.text
      parsed = f"{word.capitalize()} : {data.capitalize()}"      
      report = report + parsed

  else:
    print("The source can't be accessed.")

  return report