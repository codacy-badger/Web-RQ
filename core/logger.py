#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import datetime
import time

from core import consts


def log(message):
    """
    Funcao basica para controlar os "logs".
    :param message: Mensagem que aparecera no terminal
    :return: None
    """

    if consts.TERMINAL_LOG:
        print(message)

    else:

        with open('terminal_log', 'a', encoding='utf-8') as f:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')
            f.write(st + "\n" + message + "\n")
