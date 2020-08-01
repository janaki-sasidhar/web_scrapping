import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
ttl_lst = []
text=requests.get(url).content
soup=BeautifulSoup(text,"lxml")
print(soup.title.text)


article=soup.find("div",class_="css-6p6lnl")
print(article.span.text)

for i in soup.find_all("div",class_="css-6p6lnl"):

    #print(i.a.prettify()) to print the prettified required content
    print(f"\n {' -- '*20}\n")
    headline = i.a.get('aria-label')
    permalink = i.a.get('href')
    print(f"HEADLINE      : {headline}")
    print()
    print(f"PERMALINK IS  : http://nytimes.com{permalink}")
    print()
    print("The sub headings of the article are : ")
    print()
    for sub in article.find_all("li"):
        print(f"   -> {sub.text}")
