#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
class FindDriverDownloadException(Exception):
    pass


class FindDriverDownload(object):
    """
    Classe para obter link de download do driver.
    """

    __driver = 'geckodriver'
    __version = '0.20.1'

    @staticmethod
    def get_url(driver, version, so, bits) -> str:

        """
        Verificacao de pacote e link de download.

        :param driver: str
        :param version: str
        :param so: str
        :param bits: int
        :return: str
        """

        packages = FindDriverDownload.get_packages()
        package = ""

        if driver in packages:

            if version in packages[driver]:

                if so in packages[driver][version]:

                    if bits in packages[driver][version][so]:

                        package = packages[driver][version][so][bits]

                    else:

                        raise FindDriverDownloadException(
                            "Download do driver [{}] [v{}] [{}] não foi encontrado para [{}bits]".format(driver,
                                                                                                         version, so,
                                                                                                         bits
                                                                                                         ))
                else:

                    raise FindDriverDownloadException(
                        u"Download do driver [{}] [v{}] para [{}] não foi encontrado".format(driver, version, so))
            else:

                raise FindDriverDownloadException(
                    u"Versão [{}] do driver [{}] não foi encontrada.".format(version, driver))

        else:

            raise FindDriverDownloadException(u"Driver [{}] não encontrado para download".format(driver))

        return package

    @staticmethod
    def get_packages() -> dict:

        """
        Links de download
        :return: dict
        """

        packages = {
            'geckodriver': {
                '0.20.1': {
                    'linux': {
                        32: 'https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux32.tar.gz',
                        64: 'https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz'
                    },
                    'win': {
                        32: 'https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-win32.zip',
                        64: 'https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-win64.zip'
                    }
                }
            }
        }

        return packages

    @staticmethod
    def get_available_packages() -> list:

        return list(FindDriverDownload.get_packages().keys())
