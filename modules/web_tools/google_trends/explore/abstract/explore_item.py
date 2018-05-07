#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from modules.web_tools.google_trends.tools.geo import Geo


class AbstractExploreItem(Geo):
    __metaclass__ = ABCMeta

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
    def _item_dict(self):
        return {
            "keyword": self.keyword,
            "geo": self.geo,
            "time": self.time
        }
