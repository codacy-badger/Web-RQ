#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from modules.social_media.facebook.elements.post_elements import PostElements
from modules.social_media.facebook.actions.post.initializer import PostInitializer
from core.logger import log


class PostDataFt(PostInitializer):
    def __init__(self, shadow_class: PostInitializer):
        PostDataFt = shadow_class

    def extract(self):

        import codecs
        log(u"Obtendo dados base do post.")
        element = PostElements.get_post_data(PostDataFt.get_web_driver())

        if element:
            data_ft = element.get_attribute('data-ft')

        if data_ft:
            with codecs.open(self.get_data_ft_file(), mode='w', encoding="utf-8") as f:
                f.write(data_ft)

            log(u"Dados base salvos em: [{}]".format(self.get_data_ft_file()))

        return self

    def get_data_ft_file(self) -> str:
        return PostDataFt.get_save_path() + '/data-ft.json'

    def get_data_ft_dict(self) -> dict:
        from os.path import isfile
        from json import load
        import codecs

        dict_ret = {}

        if isfile(self.get_data_ft_file()):
            dict_ret = load(codecs.open(self.get_data_ft_file(), "r", encoding="utf-8"))

        return dict_ret
