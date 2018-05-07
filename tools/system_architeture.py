#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import platform
import sys

from core.consts import FORCE_SYSTEM_BITS


class SystemArchiteture(object):
    """
    Classe para obter dados basicos do SO.
    """

    @staticmethod
    def get_operational_system() -> str:
        return platform.architecture()[1]

    @staticmethod
    def get_bits() -> int:

        if FORCE_SYSTEM_BITS:

            bits = FORCE_SYSTEM_BITS

        else:

            bits = 64 if sys.maxsize > 2 ** 32 else 32

        return bits
