#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Constantes para uso geral do Exploit
"""

"""
    # Podemos mostrar mensagens de progresso no terminal ? 
"""
TERMINAL_LOG = True

"""
    # Versao do driver Mozilla para download
"""
GECKO_DRIVER_VERSION = '0.20.1'

"""
    # Porta para uso do driver Mozilla
"""
GECKO_DRIVER_PORT = 4444

"""
    # Qual driver usar por padrao ?
"""

DEFAULT_DRIVER = 'geckodriver'

"""
    # Se tiver com problemas no download do driver, preencha as variaveis abaixo
"""
FORCE_SYSTEM_BITS = None  # Quantos bytes seu S.O usa? | Valor padrao: None
