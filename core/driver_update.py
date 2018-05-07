#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from core import consts
from core.logger import log
from tools.file_download import FileDownload
from tools.find_driver_download import FindDriverDownload
from tools.system_architeture import SystemArchiteture
from tools.zip import Zip


class DriverUpdate(object):

    """
    Classe para atualizacao do driver que sera utilizado
    """

    # Nome do pacote
    __package = 'geckodriver'

    # Arquivo Final
    __file_name = ''

    def download(self, package='geckodriver') -> bool:

        """
        Metodo responsavel por fazer o download de determinado driver
        :param package: str Driver que vamos baixar
        :return: bool

        """

        self.set_package(package)

        log('Atualizando {}{}'.format(self.get_package(), '.'))

        download_url = self.get_url()
        self.__file_name = self.get_file_name(download_url)

        log("Fazendo download...")
        FileDownload.download(download_url, self.__file_name)
        self.uncompress()
        return True

    def uncompress(self):
        log("Descompactando...")
        import tarfile
        if tarfile.is_tarfile(self.__file_name):
            tar = tarfile.open(self.__file_name)
            tar.extractall()
            tar.close()
        else:
            Zip.unzip(self.__file_name)

    def set_package(self, package):
        self.__package = package

    def get_package(self):
        return self.__package

    def get_file_name(self,url) -> str:

        """
        Metodo responsavel por retornar o nome do arquivo final.
        :return: str Arquivo Final
        """
        from urllib.parse import urlparse
        import os

        file = os.path.basename(urlparse(url).path)

        return file

    def get_url(self) -> str:

        """
        Neste metodo vamos obter a url de download dos drivers
        :return: str Url de Download
        """

        so = SystemArchiteture.get_operational_system()
        bits = SystemArchiteture.get_bits()

        if self.__package == 'geckodriver':

            # Versao do Gecko
            vers = consts.GECKO_DRIVER_VERSION

            # Vamos trabalhar apenas com Windows e Linux

            plat = 'win' if so == 'WindowsPE' else 'linux'

            log(u"Estamoso buscando um driver para seu sistema {0}".format(plat))

            url = FindDriverDownload.get_url(self.__package, vers, plat, bits)

            log(u"A URL encontrada foi: [{0}]".format(url))

        return url
