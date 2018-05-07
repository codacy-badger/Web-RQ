#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class ExceptionGeo(Exception):
    pass


class Geo(object):
    __metaclass__ = ABCMeta
    __api_url = "https://trends.google.com.br/trends/api/explore/pickers/geo"
    __language = "pt-BR"
    __timezone = 180

    __geo_locales = None

    @property
    @abstractmethod
    def locales(self) -> dict:
        if not self.__geo_locales:

            import requests
            from modules.web_tools.google_trends.tools.url_setter import UrlSetter

            url = UrlSetter.gen_url(self.__api, self.__params)
            response = requests.get(url)

            if response.status_code != 200:
                raise ExceptionGeo("Status Code: {0}".format(response.status_code))

            from modules.web_tools.google_trends.tools.fix import Fix
            import json

            self.__geo_locales = json.loads(Fix.google_json(response.text))

        return self.__geo_locales

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