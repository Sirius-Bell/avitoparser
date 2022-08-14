#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.10.5

from selenium import webdriver
from bs4 import BeautifulSoup
from typing import Optional, Dict, List, Union


class AvitoParser:

    def __init__(self, city: str = "moskva", page: int = 1, driver: str = "chrome") -> None:
        """
        This library will help you parse the necessary data from the Avito website
        :param city: City to search for
        :param page: Page to start from
        :param driver: Driver for selenium, on default uses chrome driver
        """

        if driver == "firefox":
            self.driver: webdriver.Firefox = webdriver.Firefox()
        else:
            self.driver: webdriver.Chrome = webdriver.Chrome()

        self.city: str = city
        self.page: int = page
        self.soup: Optional[BeautifulSoup] = None

    def __str__(self) -> str:
        """
        String implementation of class AvitoParser
        :return: String
        """

        return 'AvitoParser(city=%s, page=%s, driver=%s)' % (self.city, self.page, self.driver)

    def generate_search_url(self, query: str) -> str:
        """
        This function generates an url to search the advertisement
        :param query: String, what to find
        :return: String, return the url
        """

        url: str = "https://avito.ru/%s?q=%s&p=%s" % (self.city, query, self.page)
        return url

    def get_in_avito(self, url: str) -> None:
        """
        This function visits the site Avito and transmits data to bs4
        :param url: String, url to get in
        :return: None
        """

        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source)

    def parse(self) -> List[Union[Dict[str, int], Dict[str, str]]]:
        """
        This function parse the Avito website and return a data
        :return: Dict, return the parse data
        """


# https://avito.ru/sankt-peterburg
# https://avito.ru/sankt-peterburg/kvartiry/prodam-ASgBAgICAUSSA8YQ
