#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class ExceptionAutocomplete(Exception):
    pass

class Autocomplete(object):
    __metaclass__ = ABCMeta
    __hl: str = "pt-BR"
    __tz: int = 180
    __api_url = "https://trends.google.com.br/trends/api/autocomplete/{0}"


    def query(self, q: str) -> dict:
        from modules.web_tools.google_trends.tools.url_setter import UrlSetter
        from modules.web_tools.google_trends.tools.fix import Fix
        import requests

        url = UrlSetter.gen_url(self.__api_url.format(q), {"hl": self.language, "tz": self.timezone})
        response = requests.get(url)

        if response.status_code == 200:
            json_str = Fix.google_json(response.text)
        else:
            raise ExceptionAutocomplete("Status Code: {0}".format(response.status_code))

        import json
        return json.loads(json_str)

    @property
    def language(self) -> str:
        return self.__hl

    @language.setter
    def language(self, language: str):
        self.__hl = language

    @property
    def timezone(self) -> int:
        return self.__tz

    @timezone.setter
    def timezone(self, timezone: int):
        self.__tz = timezone