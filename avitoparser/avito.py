#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11.4

import csv
from typing import Optional, List
from urllib.parse import quote

import bs4.element
from bs4 import BeautifulSoup
from selenium import webdriver

from exceptions import PageSourceNotConfigured
from loguru import logger
from model import Advert


class AvitoParser:

    def __init__(self, city: str = "moskva", page: int = 1,
                 driver: str = "chrome", export_csv: bool = True,
                 filename_to_export: str = "avitoparser_output.csv") -> None:
        """
        This library will help you parse the necessary data from the Avito
        :param city: City to search for
        :param page: Page to start from
        :param driver: Driver for selenium, on default uses chrome driver
        """

        self.rows: List[str] = ['Title', 'Description', 'Price']
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
        self.filename_to_export: str = filename_to_export
        self.export_csv: bool = export_csv

        self.__logger = logger
        self.__logger.info("Starts the avitoparser...")

    def __str__(self) -> str:
        """
        String implementation of class AvitoParser
        :return: String
        """

        return 'AvitoParser(city=%s, page=%s, driver=%s)' % (
            self.city, self.page, self.driver)

    def generate_search_url(self, query: str, sort: Optional[str] = None,
                            owner: Optional[str] = None,
                            with_images: bool = False) -> str:
        """
        This function generates an url to search the advertisement
        :param query: String, what to find
        :param sort: String, sort adverts:
            'date' - date sorting
            'price' - price sorting
            'price_desc' - price descending
            'None' - default value
        :param owner: String, owners advert:
            'private' - private advert
            'company' - company advert
            'None' - default value
        :param with_images: Boolean, with images or not
        :return: String, return the url
        """

        urlencoded_quote = quote(query)
        sort_values = {'date': '104', 'price': '1', 'price_desc': '2',
                       None: '101'}
        owners = {'private': '1', 'company': '2', None: '0'}

        url: str = "https://avito.ru/%s?q=%s&p=%s&i=%s&s=%s&user=%s" % (
            self.city, urlencoded_quote, self.page, int(with_images),
            sort_values[sort], owners[owner])
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

        self.__logger.info("Goto parse phase...")

    def save_in_csv(self, items: List[Advert]) -> None:
        """
        This function exports csv table
        :param items: List[Advert], it's an adverts
        :return: None
        """
        with open(self.filename_to_export, 'a', encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.rows)
            for advert in items:
                writer.writerow(
                    [advert.title, advert.description, f"{advert.price:_}"])

    def _parse_block(self, item: bs4.element.Tag) -> Advert:
        """
        This function parse the block of advert
        :param item: bs4.element.Tag, block of advert
        :return: Advert
        """
        try:
            description: str = item.find('div', attrs={
                'class': 'iva-item-descriptionStep-C0ty1'}).get_text()
            price_step = item.find('div',
                                   attrs={'class': 'iva-item-priceStep-uq2CQ'}) \
                .find('meta', attrs={'itemprop': 'price'}).get('content')
            title: str = item.find('div',
                              attrs={'class': 'iva-item-title-py3i_'}).find(
                'h3').get_text()
        except AttributeError:
            self.__logger.critical("Attribute error: NoneType")
            description = "Error"
            price_step = -1
            title = "Error"

        return Advert(title=title, price=int(price_step),
                      description=description)

    def parse(self) -> Optional[List[Advert]]:
        """
        This function parse the Avito website and return a data
        :return:
        List[Advert], return the parse data or None if export_csv is True
        """

        self.list_adverts = []

        if self.soup is None:
            self.__logger.critical("soup is None")
            raise PageSourceNotConfigured(
                "Run the get_in_avito() function first")

        container: bs4.element.ResultSet = self.soup.select(
            selector=self.selector)
        for item in container:
            self.list_adverts.append(self._parse_block(item))

        self.page += 1
        self.__logger.info(f"Page +1: {self.page}")
        self.__logger.info("Successful")

        if self.export_csv is True:
            self.save_in_csv(list(set(self.list_adverts)))
            return

        return list(set(self.list_adverts))


if __name__ == "__main__":
    test = AvitoParser(driver="firefox")
    for i in range(2):
        test.get_in_avito(test.generate_search_url("купить квартиру"))
        adv = test.parse()
