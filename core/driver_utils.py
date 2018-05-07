#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from core.logger import log


def check_exists_by_xpath(driver: RemoteWebDriver, xpath: str) -> bool:
    """
    Checa se o elemento existe (a partir de um XPATH)

    :param driver: RemoteWebDriver
    :param xpath: str
    :return: bool
    """
    exists = False

    try:

        driver.find_element_by_xpath(xpath=xpath)
        exists = True

    except NoSuchElementException:
        pass
        log(u"[{}] não foi encontrado.".format(xpath))

    return exists
