#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from modules.web_tools.google_trends.explore.items import ExploreItems


class ExceptionExploreRequest(Exception):
    pass


class AbstractExploreRequest(ExploreItems):
    import requests

    __metaclass__ = ABCMeta

    __session: requests.Session = None

    # = > Url de acesso base ao trends, é necessário acessa-la para que o token seja válido
    __main_url = "https://trends.google.com.br/trends/explore"

    # = > Primera requisição feita a API, nela obtemos os tokens de cada widget.
    __explore_url = "https://trends.google.com.br/trends/api/explore"

    # => Para garantirmos o acesso ao "api/explore"
    __have_main_access = False

    # = > Qual a categoria do que análisaremos?
    __category = ""

    # = > Qual a fonte que deseja análisar ?
    __source = ""

    # = > Retorno do Explore com os tokens
    __explore = None

    # = > Linguagem do retorno
    __language = "pt-BR"

    __timezone = 180

    @abstractmethod
    def __init__(self):
        # = > Vamos abrir uma sessão para garantir os tokens de cada requisição.
        self.__session = self.requests.Session()

    @property
    @abstractmethod
    def language(self) -> str:
        return self.__language

    @language.setter
    @abstractmethod
    def language(self, language: str):
        self.__language = language

    @property
    @abstractmethod
    def timezone(self) -> int:
        return self.__timezone

    @timezone.setter
    @abstractmethod
    def timezone(self, timezone: int):
        self.__timezone = timezone

    @property
    @abstractmethod
    def category(self) -> str:
        return self.__category

    @category.setter
    @abstractmethod
    def category(self, category: str):
        self.__category = category

    @property
    @abstractmethod
    def date(self) -> str:
        return self.items[0].time

    @property
    @abstractmethod
    def geo(self) -> str:
        return self.items[0].geo

    @property
    @abstractmethod
    def source(self) -> str:
        return self.__source

    @source.setter
    @abstractmethod
    def source(self, source: str):
        self.__source = source

    @property
    @abstractmethod
    def query(self) -> str:
        return ','.join(list(q.keyword for q in self.items if q.keyword))

    @abstractmethod
    def __main_access(self):
        """
        Acesso principal para garantir os Tokens
        :return: AbstractExploreRequest
        """
        if not self.__have_main_access:
            from modules.web_tools.google_trends.tools.url_setter import UrlSetter
            url = UrlSetter.gen_url(self.__main_url, self.__main_access_params)
            self.session.get(url)

        return self

    @property
    @abstractmethod
    def explore(self) -> dict:
        """
         = > Propriedade contendo os dados da primeira requisição à API
        :return: dict
        """

        if not self.__explore:
            # = > Se os dados não existirem, podemos requisita-los
            self.__main_access()
            from modules.web_tools.google_trends.tools.url_setter import UrlSetter

            # Formamos a URL para o método GET.
            url = UrlSetter.gen_url(self.__explore_url, self.__explore_params)

            response = self.session.get(url)

            if response.status_code != 200:
                raise ExceptionExploreRequest(
                    "Não foi possível obter os dados de \"explore\". \n[Status Code: {0}]".format(response.status_code))

            from modules.web_tools.google_trends.tools.fix import Fix
            import json

            # = > Corrigimos o JSON retornado pela API
            self.__explore = json.loads(Fix.google_json(response.text))

        return self.__explore

    @property
    @abstractmethod
    def __explore_params(self) -> dict:
        """
         = > Parâmetros no formato que devem ser enviados a API
        :return: dict
        """
        import json

        req = {}

        req["comparisonItem"] = self.comparison_list

        if self.category:
            req["category"] = self.category

        if self.source:
            req["property"] = self.source

        return {
            "hl": self.language,
            "tz": self.timezone,
            "req": json.dumps(req)
        }

    @property
    @abstractmethod
    def __main_access_params(self) -> dict:
        """
         # => Parâmetros do acesso principal no formato em que devem ser enviados a API
        :return: dict
        """
        return {
            "cat": self.category,
            "date": self.date,
            "geo": self.geo,
            "gprop": self.source,
            "q": self.query
        }

    @property
    @abstractmethod
    def session(self) -> requests.Session:
        return self.__session

    @property
    @abstractmethod
    def widgets(self) -> list:
        return self.explore["widgets"]
