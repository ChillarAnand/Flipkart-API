#! /usr/bin/env python

from purl import URL
import sys
from bs4 import BeautifulSoup

if sys.version_info >= (3, 0):
    from urllib.request import urlopen
else:
    from urllib2 import urlopen


class Flipkart():

    def __init__(self):
        self.base_url = 'http://www.flipkart.com'

    def search(self, query):
        url_combo = URL(self.base_url).path('search').query_param('q', query)
        results_page = urlopen(str(url_combo))
        soup = BeautifulSoup(results_page)
        search_results = soup.findAll("div", {"class" : "pu-title fk-font-13" })
        return search_results

    def list_items(self, search_results):
        items= {} 
        for result in search_results:
            if result.find("a"):
                title = result.find("a")['title']
                href = result.find("a")['href']
                url = self.base_url + href
                items[title] = url
        return items
