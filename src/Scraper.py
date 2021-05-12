'''
This scraper its for gather news form diferents sources across Newss Papers.


'''



import request as rq
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/List_of_newspapers_in_Colombia"



def make_soup(url):
    response = rq.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    return soup




def main():
    general_list = make_soup(url)



if __name__ == '__main__':
    main()


