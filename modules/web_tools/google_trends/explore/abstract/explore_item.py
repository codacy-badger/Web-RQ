#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from modules.web_tools.google_trends.tools.geo import Geo


class AbstractExploreItem(Geo):

    """
     = > Abstração de classe para itens que devem ser buscados no Trends
    """

    __metaclass__ = ABCMeta

    # = A Keyword deve ser o item que vai ser pesquisado, ex.: Carros
    # = A Keyword também pode ser o código de um item, por exemplo "BMW", relacionada a "Fabricante de Automóveis"
    # = tem o código: /m/017yh
    # = Você pode obter os códigos em tools.autocomplete, lá você poderá pesquisar um item e obter o mesmo com seu
    # = código relacionado a determinada categoria.
    __keyword = ""

    __geo = "BR"

    __time = "now 1-H"

    @property
    @abstractmethod
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    @abstractmethod
    def geo(self) -> str:
        return self.__geo

    @geo.setter
    @abstractmethod
    def geo(self, geo: str):
        self.__geo = geo

    @property
    @abstractmethod
    def time(self) -> str:
        return self.__time

    @time.setter
    @abstractmethod
    def time(self, time: str):
        self.__time = time

    @property
    @abstractmethod
    def _item_dict(self) -> dict:
        """
         = > Esta função já retorna o dict na forma que deve ser enviado aos servidores do Google.
        :return: dict
        """
        return {
            "keyword": self.keyword,
            "geo": self.geo,
            "time": self.time
        }
