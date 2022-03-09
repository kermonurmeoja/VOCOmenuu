from bs4 import BeautifulSoup
import requests

url = "https://siseveeb.voco.ee/veebivormid/restorani_menuu"

sisu = requests.get(url).text
doc = BeautifulSoup(sisu, "html.parser")

soojadtoidud = doc.find_all("tr")

for s in soojadtoidud:
    vee = s.find_all("td")
    for f in vee:
        print(f.text)
        

listike = []
#for soetoit in soojadtoidud:
 #   print(soetoit.contents[0].table, end="\n")
    
    
    
