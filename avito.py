#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.10.5

from typing import Optional, List
from urllib.parse import quote

from bs4 import BeautifulSoup
from selenium import webdriver

from exceptions import PageSourceNotConfigured
from logger import get_logger
from model import Advert


class AvitoParser:

    def __init__(self, city: str = "moskva", page: int = 1,
                 driver: str = "chrome") -> None:
        """
        This library will help you parse the necessary data from the Avito
        :param city: City to search for
        :param page: Page to start from
        :param driver: Driver for selenium, on default uses chrome driver
        """

        self.list_adverts: Optional[List[Advert]] = None
        if driver == "firefox":
            self.driver: webdriver.Firefox = webdriver.Firefox()
        else:
            self.driver: webdriver.Chrome = webdriver.Chrome()

        self.city: str = city
        self.page: int = page
        self.soup: Optional[BeautifulSoup] = None
        self.selector: str = 'div.iva-item-root-_lk9K.photo-slider-slider' \
                             '-S15A_.iva-item-list-rfgcH.' \
                             'iva-item-redesign-rop6P.iva-item-responsive' \
                             '-_lbhG.items-item-My3ih.items-listItem-Gd1jN.' \
                             'js-catalog-item-enum '

        self.__logger = get_logger(__name__, turn_file_handler=True)
        self.__logger.info("Starts the avitoparser...")

    def __str__(self) -> str:
        """
        String implementation of class AvitoParser
        :return: String
        """

        return 'AvitoParser(city=%s, page=%s, driver=%s)' % (
            self.city, self.page, self.driver)

    def generate_search_url(self, query: str) -> str:
        """
        This function generates an url to search the advertisement
        :param query: String, what to find
        :return: String, return the url
        """

        urlencoded_quote = quote(query)

        url: str = "https://avito.ru/%s?q=%s&p=%s" % (
            self.city, urlencoded_quote, self.page)
        self.__logger.debug("get URL: %s" % url)
        return url

    def get_in_avito(self, url: str) -> None:
        """
        This function visits the site Avito and transmits data to bs4
        :param url: String, url to get in
        :return: None
        """

        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'lxml')

        self.__logger.info("Init successfully")
        self.__logger.info("Goto parse phase...")

    def _parse_block(self, item):
        description: str = item.find('div', attrs={
            'class': 'iva-item-text-Ge6dR iva-item-description-FDgK4 '
                     'text-text-LurtD text-size-s-BxGpL'}).get_text()
        price_step = item.find('div',
                               attrs={'class': 'iva-item-priceStep-uq2CQ'}) \
            .find('meta', attrs={'itemprop': 'price'}).get('content')
        title = item.find('div',
                          attrs={'class': 'iva-item-titleStep-pdebR'}).find(
            'h3').get_text()

        return Advert(title=title, price=price_step, description=description)

    def parse(self) -> List[Advert]:
        """
        This function parse the Avito website and return a data
        :return: List[Advert], return the parse data
        """

        self.list_adverts = []

        if self.soup is None:
            self.__logger.critical("soup is None")
            raise PageSourceNotConfigured(
                "Run the get_in_avito() function first")

        container = self.soup.select(selector=self.selector)
        for item in container:
            self.list_adverts.append(self._parse_block(item))

        return self.list_adverts


if __name__ == "__main__":
    test = AvitoParser()
    test.get_in_avito(test.generate_search_url("купить квартиру"))
    adv = test.parse()
    print(adv)
