#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from modules.social_media.facebook.elements.post_elements import PostElements
from modules.social_media.facebook.actions.post.initializer import PostInitializer


class TextHTML(PostInitializer):
    def __init__(self, shadow_class: PostInitializer):
        TextHTML = shadow_class

    def extract(self):

        from core.logger import log
        import codecs

        log(u"Obtendo HTML do post.")

        element = PostElements.get_post_text_html(TextHTML.get_web_driver())
        html = ""

        if element:
            html = element.get_attribute('innerHTML')

        with codecs.open(self.get_html_file(), 'w', encoding="utf-8") as f:
            f.write(html)

        log(u"Texto HTML salvo em: [{}]".format(self.get_html_file()))

        return self

    def get_html_file(self):
        return TextHTML.get_save_path() + "/text.html"

    def get_html_text(self) -> str:
        html = ""

        from os.path import isfile
        import codecs

        if isfile(self.get_html_file()):
            with codecs.open(self.get_html_file(), "r", encoding="utf-8") as f:
                html = f.read()

        return html
