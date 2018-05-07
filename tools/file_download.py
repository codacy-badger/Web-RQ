#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from urllib.request import urlretrieve, urlopen

from core.logger import log


class FileDownload(object):
    """
    Ferramenta para fazer download de um arquivo e ter o report_hook
    """

    @staticmethod
    def download(url, file_name: str = ""):

        """
        Funcao que faz o download.

        :param url: str
        :param file_name: str
        :return: None
        """

        urlretrieve(url, file_name, FileDownload.__report_hook)

    @staticmethod
    def get_format(url: str) -> str:

        """
        Funcao para obter formato de um arquivo na Web.

        :param url: str
        :return: str
        """

        remote_file = urlopen(url)
        extension = ""

        try:
            extension = str(remote_file.info()['content-type']).split("/")[1]
        except:
            extension = str(remote_file.info()['content-type']).split("/")[0]

        return extension

    @staticmethod
    def __report_hook(blocknum, blocksize, totalsize):

        """
        Metodo para monitorar o andamento do download.
        Peguei de https://stackoverflow.com/questions/13881092/download-progressbar-for-python-3
        """

        readsofar = blocknum * blocksize

        if totalsize > 0:

            percent = readsofar * 1e2 / totalsize

            s = "\r%5.1f%% %*d / %d" % (
                percent, len(str(totalsize)), readsofar, totalsize)

            log(s)

            if readsofar >= totalsize:  # near the end
                log('\n')
        else:  # total size is unknown
            log("read %d\n" % (readsofar,))
