import requests
from bs4 import BeautifulSoup

url = 'http://www.sakshi.com/andhra-pradesh'
text=requests.get(url).content
soup=BeautifulSoup(text,"lxml")
print(soup.title.text)
#views-field views-field-title
article=soup.find("div",class_="views-field views-field-title")
print(article)
for i in soup.find_all("div",class_="views-field views-field-title"):
    print(f"The headline is   :  {i.a.text}")
    print(f" The premalink is :  http://www.sakshi.com/{i.a.get('href')}")
    print()
    print( ' - '*20)



