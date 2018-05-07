#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class AbstractLatest(object):
    __metaclass__ = ABCMeta
    __lang: str = "pt-BR"
    __timezone: int = 180
    __category: str = "all"
    __geo: str = "BR"
    __sort: bool = False
    __google_api_url = "https://trends.google.com.br/trends/api/stories/latest"

    # Não descobri o que são estes abaixo :/

    __fi: int = 15
    __fs: int = 15
    __ri: int = 300
    __rs: int = 15

    @property
    @abstractmethod
    def _params(self) -> dict:
        return {
            "hl": self.lang,
            "tz": self.timezone,
            "cat": self.category,
            "geo": self.geo,
            "sort": int(self.sort),
            "fi": self.fi,
            "fs": self.fs,
            "ri": self.ri,
            "rs": self.rs
        }

    @property
    @abstractmethod
    def _api_url(self) -> str:
        return self.__google_api_url

    @property
    @abstractmethod
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    @abstractmethod
    def lang(self, lang: str):
        self.__lang = lang

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
        self.category = category

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
    def sort(self) -> bool:
        return self.__sort

    @sort.setter
    @abstractmethod
    def sort(self, sort: bool):
        self.__sort = sort

    @property
    @abstractmethod
    def fi(self) -> int:
        return self.__fi

    @fi.setter
    @abstractmethod
    def fi(self, fi: int):
        self.__fi = fi

    @property
    @abstractmethod
    def fs(self) -> int:
        return self.__fs

    @fs.setter
    @abstractmethod
    def fs(self, fs: int):
        self.__fs = fs

    @property
    @abstractmethod
    def ri(self) -> int:
        return self.__ri

    @ri.setter
    @abstractmethod
    def ri(self, ri: int):
        self.__ri = ri

    @property
    @abstractmethod
    def rs(self) -> int:
        return self.__rs

    @rs.setter
    @abstractmethod
    def rs(self, rs: int):
        self.__rs = rs
