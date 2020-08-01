from bs4 import BeautifulSoup
import requests

#create a requests object and read the contents
fo=requests.get("https://www.sasidhar.wtf").content

#create a soup object and parse 
soup = BeautifulSoup(fo, 'lxml')

#The trick is to test for one article using soup.find and apply the loop for soup.find_all
for article in soup.find_all("ul",class_="post-list"):

    #The reason for subitems is there are the non-classed li in the <div></div> thig we are using for find all. And if we find directly using findall, it is considering the li which has class attributes . so this trick is used.
    subitems=article.find_all("li")
    for i in subitems:
        print(f"The title is : \n {i.h2.a.text}")
        print()
        print(f"The description is : \n {i.p.text}")
        print()
        print(f"The permalink is :  \nhttps://www.sasidhar.wtf{i.a.get('href')}")
        print()
        print(' - '*20)
        print()



