'''
This scraper its for gather news form diferents sources across Newss Papers.


'''
from os import link
import requests as rq
from bs4 import BeautifulSoup

#Las diferentes páginas de la oreja




""" def make_soup(url, pag=""):
    response = rq.get(url)
    response = response.text
    soup = BeautifulSoup(response, "html.parser")
    return soup
 """

url = "https://www.laorejaroja.com/type/opina/"
response = rq.get(url)
response = response.text
soup = BeautifulSoup(response, "html.parser")

#containers = soup.find_all()
#print(type(containers))
l#ink = containers.find('a', 'href')
#print(link)

for link in soup.find('div', {'class':'image uniform'}).find_all('a', 'href'):
    if 'href' in link.attrs:
        print(link.attrs['href'])




#if __name__ == '__main__':
"""     pages =['opina','informate','narra']
    for page in pages:
        s = make_soup("https://www.laorejaroja.com/type"+ page)
        print(s)
        print("▬"*100)
     """
    #pass
    


