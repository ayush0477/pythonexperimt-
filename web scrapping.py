import bs4 as bs
import urllib.request
sause = urllib.request.urlopen('https://www.google.com/').read()
soup = bs.BeautifulSoup(sause,'lxml')
print(sause.title.text)