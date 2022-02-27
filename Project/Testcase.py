import unittest
import requests
from bs4 import BeautifulSoup
import urllib
import urllib.request
import re

# Testing the passing of the html string
class Test(unittest.TestCase):
    def test_program(self):
        with urllib.request.urlopen('http://192.168.1.3/spicyx/') as response:
            html = response.read()
            soup = BeautifulSoup(html, 'lxml')
            type(soup)
            print(soup.prettify()[0:100])
            text_only = soup.get_text()
            print(text_only)
            soup.find_all("li")


# Testing response of website
class Scrapytest(unittest.TestCase):
    def testweb(self):
        url = "http://192.168.1.3/spicyx/"
        r = requests.get(url)
        if (r.status_code == 200):
            print('Website Can Reponse')
        else:
            print ('Website Cannot Reponse')
        r.close()
        Websource = r.content
        print(Websource)


if __name__ == '__main__':
    unittest.main()