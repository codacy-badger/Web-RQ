#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import platform
from subprocess import Popen
import os
from core import consts, logger

"""
@deprecated
"""
class DriverStandalone(object):
    __process = None


    def server(self, package='geckodriver'):
        so = self.__get_so()
        # extension = 'exe' if so == 'WindowsPE' else ''

        self.__process = Popen([package, '-p', str(consts.GECKO_DRIVER_PORT), '&'],
                               shell=True)

    def __get_so(self) -> str:
        """
        Funcao especifica para retornar o nome do SO atual.
        :return: str SO Name
        """
        return platform.architecture()[1]

    def close(self):
        if self.__process:
            self.__process.terminate()

    def __del__(self):
        self.close()
