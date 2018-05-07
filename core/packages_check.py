#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from setuptools.command.easy_install import main as install
SELENIUM_PACKAGES = [
    'facebook-sdk',
    'pip',
    'selenium',
    "requests"
]

TOTAL_PACKAGES = len(SELENIUM_PACKAGES)

i = 0

for i in range(0, TOTAL_PACKAGES):
    PACKAGE = SELENIUM_PACKAGES[i]
    install([PACKAGE])
