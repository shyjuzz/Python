import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
response =  urllib.request.urlopen('https://www.nltk.org/book/ch01.html')
html = response.read()
soup = BeautifulSoup(html)
text = soup.get_text(strip = True)
tokens = [t for t in text.split()]
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):

        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)
