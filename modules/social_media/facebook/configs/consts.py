#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""
Constantes para uso no Facebook.
"""


FACEBOOK_API_VERSION = "2.12"

"""
    # URL DE LOGIN 
"""
FACEBOOK_LOGIN_URL = 'https://mbasic.facebook.com/'

"""
    # URL PARA CANCELAR A REQUISICAO PARA SALVAR O DISPOSITIVO 
"""
FACEBOOK_CANCEL_SAVE_DEVICE = FACEBOOK_LOGIN_URL + 'login/save-device/cancel/?flow=interstitial_nux&amp;nux_source=regular_login'

"""
    # URL PARA CANCELAR A REQUISICAO DO TELEFONE 
"""
FACEBOOK_PHONE_SKIP = FACEBOOK_LOGIN_URL + 'a/nux/wizard/nav.php?step=phone&skip'

"""
    # URL PARA CANCELAR A REQUISICAO DE BUSCA DE AMIGOS 
"""
FACEBOOK_SEARCH_SKIP = FACEBOOK_LOGIN_URL + 'a/nux/wizard/nav.php?step=search&skip'

"""
    # PARTE DE URL PARA IDENTIFICAR PASSO DE SALVAR O DISPOSITIVO 
"""
FACEBOOK_SAVE_DEVICE_CHECK = 'save-device'

"""
    # PARTE DE URL PARA IDENTIFICAR SE A CONTA FOI BLOQUEADA OU ESTA EM UM CHECKPOINT 
"""
FACEBOOK_BLOCK_OR_CHEKCPOIN_CHECK = 'checkpoint' # O erro nao foi proposital, depois corrijo

"""
    # PARTE DE URL PARA IDENTIFICAR SE A CONTA ESTA NOS PASSOS INICIAIS 
"""
FACEBOOK_ACCOUNT_START_CHECK = 'gettingstarted'

"""
    # PARTE DE URL PARA IDENTIFICAR SE A CONTA ESTA NA BUSCA POR AMIGOS 
"""
FACEBOOK_STEP_SEARCH_CHECK = 'step=search'