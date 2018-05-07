#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from modules.web_tools.google_trends.explore.item import ExploreItem
from typing import List


class ExploreItems(object):
    """
     # = > Classe para manipulação dos itens que serão requisitados.
    """
    __items = []

    def new_item(self, keyword: str, geo: str = "", time: str = "now 1-H") -> ExploreItem:
        """
        # = > Função para criamos um novo item.
        :param keyword: str
        :param geo: str
        :param time: str
        :return: ExploreItem
        """
        item = ExploreItem()
        item.keyword = keyword
        item.geo = geo
        item.time = time

        return item

    def add_item(self, item: ExploreItem):
        """
        Adicionamos um novo item para a lista.
        :param item: ExploreItem
        :return: self
        """
        self.__items.append(item)
        return self

    @property
    def items(self) -> List[ExploreItem]:
        return self.__items

    @items.setter
    def items(self, items: List[ExploreItem]):
        self.__items = items

    @property
    def comparison_list(self) -> List[dict]:
        comparison: List[dict] = []

        for item in self.items:
            comparison.append(item._item_dict)

        return comparison
