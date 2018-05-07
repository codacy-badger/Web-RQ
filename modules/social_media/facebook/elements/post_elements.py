#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webdriver import WebElement

from core.driver_utils import check_exists_by_xpath
from modules.social_media.facebook.book.post_book import XPATH_POST_CONTAINER, XPATH_POST_CONTAINER_TOP, \
    XPATH_POST_CONTAINER_TOP_DATA, XPATH_POST_CONTAINER_TOP_DATA_TEXT, XPATH_POST_CONTAINER_TOP_DATA_TEXT_HTML, \
    XPATH_POST_CONTAINER_TOP_DATA_VIDEO, XPATH_PAGE_POST_REACTIONS, XPATH_PAGE_POST_REACTIONS_COLS


class PostElements:
    """
    Classe para obter elementos de postagem
    """

    @staticmethod
    def get_container(driver: RemoteWebDriver) -> WebElement:

        """
        Funcao para obter container do post
        :param driver: RemoteWebDriver
        :return: WebElement
        """

        if check_exists_by_xpath(driver, XPATH_POST_CONTAINER):
            return driver.find_element_by_xpath(XPATH_POST_CONTAINER)

    @staticmethod
    def get_container_top(driver: RemoteWebDriver) -> WebElement:

        """
        Funcao para obter o topo do container do post
        :param driver: RemoteWebDriver
        :return: WebElement
        """

        container = PostElements.get_container(driver=driver)

        if check_exists_by_xpath(container, XPATH_POST_CONTAINER_TOP):
            return container.find_element_by_xpath(XPATH_POST_CONTAINER_TOP)

    @staticmethod
    def get_post_data(driver: RemoteWebDriver) -> WebElement:

        """
        Obtem div com dados do post
        :param driver: RemoteWebDriver
        :return: WebElement
        """

        container_top = PostElements.get_container_top(driver)

        if check_exists_by_xpath(container_top, XPATH_POST_CONTAINER_TOP_DATA):
            return container_top.find_element_by_xpath(XPATH_POST_CONTAINER_TOP_DATA)

    @staticmethod
    def get_post_text_box(driver: RemoteWebDriver) -> WebElement:

        """
        Funcao para obter div com texto do post
        :param driver: RemoteWebDriver
        :return: WebElement
        """

        post_data = PostElements.get_post_data(driver)

        if check_exists_by_xpath(post_data, XPATH_POST_CONTAINER_TOP_DATA_TEXT):
            return post_data.find_element_by_xpath(XPATH_POST_CONTAINER_TOP_DATA_TEXT)

    @staticmethod
    def get_post_text_html(driver: RemoteWebDriver) -> WebElement:

        """
        Funcao para obter div com o HTML do texto da postagem.
        :param driver: RemoteWebDriver
        :return: WebElement
        """

        post_text_box = PostElements.get_post_text_box(driver)

        if check_exists_by_xpath(post_text_box, XPATH_POST_CONTAINER_TOP_DATA_TEXT_HTML):
            return post_text_box.find_element_by_xpath(XPATH_POST_CONTAINER_TOP_DATA_TEXT_HTML)

    @staticmethod
    def get_post_video(driver: RemoteWebDriver) -> WebElement:

        """
        Funcao para obter o video de uma postagem

        :param driver: RemoteWebDriver
        :return: WebElement
        """

        post_data = PostElements.get_post_data(driver)

        if check_exists_by_xpath(post_data, XPATH_POST_CONTAINER_TOP_DATA_VIDEO):
            return post_data.find_element_by_xpath(XPATH_POST_CONTAINER_TOP_DATA_VIDEO)

    @staticmethod
    def get_post_reactions_lines(driver: RemoteWebDriver):

        """
        :rtype: list of WebElement
        """

        if check_exists_by_xpath(driver, XPATH_PAGE_POST_REACTIONS):
            return driver.find_elements_by_xpath(XPATH_PAGE_POST_REACTIONS)

    @staticmethod
    def get_post_reactions_lines_collumns(element: WebElement):

        """
        :rtype: list of WebElement
        """



        if check_exists_by_xpath(element, XPATH_PAGE_POST_REACTIONS_COLS):
            return element.find_elements_by_xpath(XPATH_PAGE_POST_REACTIONS_COLS)

    @staticmethod
    def get_post_reactions_lines_collumn_reaction(elements) -> str:
        """

        :param elements: list of WebElement
        :return: str
        """

        reaction = ""
        try:
            reaction = elements[2].find_element_by_tag_name("img").get_attribute('alt')
        except IndexError:
            pass

        return reaction

    @staticmethod
    def get_post_reactions_lines_collumn_user_name(elements) -> str:

        name = ""

        try:
            name = elements[3].find_element_by_tag_name("a").text
        except IndexError:
            pass

        return name

    @staticmethod
    def get_post_reactions_lines_collumn_link(elements) -> str:
        link = ""

        try:
            link = elements[3].find_element_by_tag_name("a").get_attribute("href")
        except IndexError:
            pass

        return link
