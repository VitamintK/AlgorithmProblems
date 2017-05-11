import requests
import bs4
BASE = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/"
q = ['qds.html']
visited = set()
visited.add(q[0])
words = []
while len(q) >0:
    p = BASE + q.pop()
    g = requests.get(p).text
    soup  = bs4.BeautifulSoup(g)
    if 'Secret' in soup.text.split():
        print(soup.text.split()[3])
        words.append(soup.text.split()[3])
    for tag in soup.find_all('a'):
        link = tag.get('href',None)
        if link is not None:
            if link not in visited:
                q.append(link)
                visited.add(link)

for word in sorted(words):
    print(word)
