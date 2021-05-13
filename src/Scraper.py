'''
This scraper its for gather news form diferents sources across Newss Papers.


'''
import pandas as pd  
import requests as rq
from bs4 import BeautifulSoup


def read_file():
    df = pd.read_csv('', names=['Name', 'City','URL'])
    return df



def make_soup(url):
    response = rq.get(url)
    response.s
    soup = BeautifulSoup(response, "html.parser")
    return soup




def main():
    df = read_file()
    for newspaper in df:
        print(df['URL'])
    



if __name__ == '__main__':
    main()


