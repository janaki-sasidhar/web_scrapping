from bs4 import BeautifulSoup
import requests
fo=requests.get("https://lushka.al/posts").content
soup = BeautifulSoup(fo, 'lxml')
i=0
for article in soup.find_all("li",class_="post-item"):
    #article=soup.find("li",class_="post-item")
    post_title=article.a.span.text
    post_link=article.a.get('href')
    post_date=soup.find_all("span",class_="post-day")[i].text
    i=i+1
    print(post_link)
    print(post_title)
    print(post_date.lstrip())
    print('*'*20)

print(i)
