import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?tbs=lf:1,lf_ui:9&tbm=lcl&q=restaurants+near+me&rflfq=1&num=10&sa=X&ved=2ahUKEwiHrbiE29X9AhU9mFYBHWXuAzgQjGp6BAghEAE&biw=1920&bih=977&dpr=1#lpg=cid:CgIgAQ%3D%3D&rlfi=hd:;si:17393343338803830204,a;mv:[[-33.912359599999995,151.0406435],[-33.921368199999996,151.0297694]]'
html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')


results = soup.find_all("span", {"class": "OSrXXb"})
print(results)

for name in results:
    print(name.text)