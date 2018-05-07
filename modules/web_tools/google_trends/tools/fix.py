#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Fix(object):
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def google_json(string: str) -> str:

        # = > Buscamos o ínicio do JSON
        fix_json = string[string.index("{") - 1:len(string)]

        if fix_json.index("{") > 1:
            # = > Se não obtivemos ele como posição inicial, então, continuamos a busca
            # = > Eu sei, é bem improvavel que entre nesta condição.
            fix_json = Fix.google_json(fix_json)
        elif not fix_json.index("{"):
            # = > Caso o fix_json.index("{") retorne 0, ele será entendido como False, então:
            # = > elif not False
            raise ExceptionFix("Não foi possível obter uma sintaxe JSON válida.")

        return fix_json


class ExceptionFix(Exception):
    pass
