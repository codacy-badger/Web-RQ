#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class ExceptionCategories(Exception):
    pass


class Categories(object):
    """
    # = > Classe para obtenção das categorias disponíveis no explore.
    """
    __metaclass__ = ABCMeta
    __api_url = "https://trends.google.com.br/trends/api/explore/pickers/category"

    __language = "pt-BR"
    __timezone = 180

    __categories = None

    @property
    @abstractmethod
    def categories(self) -> dict:
        """
        # = > Dict com categorias disponíveis.
        :return: dict
        """

        if not self.__categories:
            # = > Se as categorias não estiverem setadas, então faremos a requisição.

            import requests
            from modules.web_tools.google_trends.tools.url_setter import UrlSetter

            # = > Construindo URL de acesso.
            url = UrlSetter.gen_url(self.__api, self.__params)
            response = requests.get(url)

            if response.status_code != 200:
                raise ExceptionCategories("Status Code: {0}".format(response.status_code))

            from modules.web_tools.google_trends.tools.fix import Fix
            import json

            self.__categories = json.loads(Fix.google_json(response.text))

        return self.__categories

    @property
    @abstractmethod
    def __api(self) -> str:
        return self.__api_url

    @property
    @abstractmethod
    def language(self) -> str:
        return self.__language

    @property
    @abstractmethod
    def timezone(self) -> int:
        return self.__timezone

    @language.setter
    @abstractmethod
    def language(self, language: str):
        self.__language = language

    @timezone.setter
    @abstractmethod
    def timezone(self, timezone: int):
        self.__timezone = timezone

    @property
    @abstractmethod
    def __params(self) -> dict:
        return {
            "hl": self.language,
            "tz": self.timezone
        }
