import requests
from bs4 import BeautifulSoup
import urllib

user=input("Enter the user name:")
link="https://www.picuki.com/profile/"+user
page=requests.get(link)
s=BeautifulSoup(page.content,'html.parser')
l=s.find_all('img')
post=[]
for i in l:
    if 'src' in i.attrs:
        print(str(i.attrs['src'])+"\n")
        post.append(str(i.attrs['src']))
link=post[0]
name=input("Enter file name")+".jpg"
urllib.request.urlretrieve(link,name)