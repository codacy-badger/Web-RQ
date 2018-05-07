#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Path para Container do POST
"""
XPATH_POST_CONTAINER = ".//div[@id=\"m_story_permalink_view\" or @id=\"objects_container\"]"

"""
PATH PARA CONTAINER TOP DO POST
"""
XPATH_POST_CONTAINER_TOP = ".//div[@class=\"y\" or @id=\"root\"]"

"""
PATH PARA DADOS DO TOP CONTAINER
"""
XPATH_POST_CONTAINER_TOP_DATA = ".//div[@id=\"u_0_0\" or @id=\"u_0_e\" or @id=\"u_0_1\"]"

"""
PATH PARA VIDEO NOS DADOS DO TOP CONTAINER
"""
XPATH_POST_CONTAINER_TOP_DATA_VIDEO = ".//div[@class=\"bq\" or @class=\"bt\"]//a"

"""
PATH PARA TEXTO NO TOP CONTAINER
"""
XPATH_POST_CONTAINER_TOP_DATA_TEXT = ".//div[@class=\"bb\" or @id=\"MPhotoContent\"]"

"""
PATH PARA HTML DE TEXTO NO TOP CONTAINER
"""
XPATH_POST_CONTAINER_TOP_DATA_TEXT_HTML = ".//div[@class=\"bh\"]//p|//div[@class=\"ca\"]"

# Patterns
"""
BASE URL PARA ACESSOS GERAIS
"""
PATTERN_PAGE_POST_BASE_URL = "https://mbasic.facebook.com/"

"""
BASE URL PARA ACESSO AO POST
"""
PATTERN_PAGE_POST = PATTERN_PAGE_POST_BASE_URL + "story.php?story_fbid={0}&id={1}"

"""
BASE URL PARA ACESSO A REACTIONS
"""
PATTERN_PAGE_POST_REACTIONS = PATTERN_PAGE_POST_BASE_URL + "ufi/reaction/profile/browser/?ft_ent_identifier={0}"

XPATH_PAGE_POST_REACTIONS = ".//li"
XPATH_PAGE_POST_REACTIONS_COLS = ".//td"



XPATH_PAGE_POST_COMMENTS_BOX = ".//div[@class=\"cf\"]"

PATTERN_PAGE_POST_COMMENTS_SEE_NEXT = ".//div[@id=\"see_next_{0}\"]//a"