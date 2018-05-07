#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import lxml.html as html
from lxml import etree


class LikesFileReader():
    __html = None
    __lines = None

    def __init__(self, file_path):
        self.__html = html.parse(file_path)

    def get_likes(self) -> list:
        return self.__parse_lines()

    def __parse_lines(self) -> list:
        self.__lines = self.__html.xpath(".//li")
        lines_count = len(self.__lines)
        likes = []

        for i in range(0, lines_count):

            line = self.__lines[i]

            collumns = line.xpath(".//td")
            colls_count = len(collumns)

            # Se for apenas um, significa "ver mais"
            if colls_count > 1:
                """
                0 = Base
                1 = Foto
                2 = Reação
                3 = Nome
                4 = Botão
                """

                likes.append({
                    "profile_name": collumns[3].text_content(),
                    "profile_url": "https://fb.com{0}".format(collumns[3].xpath(".//a")[0].get("href")),
                    "reaction_img": collumns[2].xpath(".//img")[0].get("src"),
                    "reaction": collumns[2].xpath(".//img")[0].get("alt")
                })

        return likes

