#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import argparse

from tools.find_driver_download import FindDriverDownload

"""
Script para leitura de argumentos passados ao client.
"""

parser = argparse.ArgumentParser()

"""
Update do driver configurado.
"""
parser.add_argument('-du', '--driver-update', default="", choices=FindDriverDownload.get_available_packages(),
                    help=u"atualiza o driver em questão")

parser.add_argument("-pu", "--packages-check", action="store_true",
                    help=u"verifica se todos os pacotes necessários estão atualizados.")

# Obtem argumentos
args = parser.parse_args()


if ('driver_update' in args) and args.driver_update:
    driver_update = args.driver_update
    from core.driver_update import DriverUpdate

    updater = DriverUpdate()
    updater.download(package=driver_update)
    del updater
    exit(0)

if args.packages_check:
    import core.packages_check
    exit(0)