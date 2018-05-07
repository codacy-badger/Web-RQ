#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from core.consts import DEFAULT_DRIVER
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DriverRequestException(Exception):
    pass


class DriverRequest(object):
    """
    Classe para requisicao de drivers
    """

    # Instancia
    __driver_instance = None

    def get_driver(self, driver=DEFAULT_DRIVER) -> RemoteWebDriver:
        """

        Funcao para requisitar um driver especifico
        :param driver: Driver que deve ser requisitado
        :return: RemoteWebDriver

        """
        self.__driver_instance = None

        import sys
        from os.path import dirname,abspath

        from tools.system_architeture import SystemArchiteture
        extension = '.exe' if SystemArchiteture.get_operational_system() == 'WindowsPE' else ''
        fname = driver+"{0}".format(extension)
        path = dirname(abspath(sys.argv[0]))+'/{0}'.format(fname)

        if driver == 'geckodriver':
            cap = DesiredCapabilities().FIREFOX
            self.__driver_instance = webdriver.Firefox(executable_path=path,capabilities=cap)

        else:
            raise DriverRequestException(u"O driver [{}] não pode ser instanciado.".format(driver))

        return self.__driver_instance
