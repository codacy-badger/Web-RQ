#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from modules.social_media.facebook.elements.post_elements import PostElements
from modules.social_media.facebook.actions.post.initializer import PostInitializer
from modules.social_media.facebook.book.post_book import PATTERN_PAGE_POST_REACTIONS
from core.logger import log


class PostReactions(PostInitializer):
    __extended: bool = False

    def __init__(self, shadow_class: PostInitializer):
        PostReactions = shadow_class

    def extract(self):

        if not self.__extended:
            log(u"Carregando reações")
            PostReactions.get_web_driver().get(PATTERN_PAGE_POST_REACTIONS.format(PostReactions.get_post_id()))

        lines = PostElements.get_post_reactions_lines(PostReactions.get_web_driver())

        lines_count = len(lines)

        if not self.__extended and lines_count > 0:
            log(u"Carregando reações extendidas")

            more = str(lines[lines_count - 1].find_element_by_tag_name("a").get_attribute("href")).replace(
                "limit=10", "limit=1000000")

            PostReactions.get_web_driver().get(more)

            self.__extended = True
            self.extract()
            self.__extended = False

        if lines_count > 0 and self.__extended:
            log(u"Salvando reações")

            import codecs

            with codecs.open(self.get_likes_file(), "w", encoding="utf-8") as infile:
                page_source = PostInitializer.get_web_driver().page_source
                infile.write(page_source)

            log(u"Reações salvas em: [{0}]".format(self.get_likes_file()))

        return self

    def get_likes_file(self) -> str:
        return PostReactions.get_save_path() + "/likes.html"

    def get_reactions_list(self) -> list:

        from modules.social_media.facebook.helper.likes_file_reader import LikesFileReader

        likes_reader = LikesFileReader(self.get_likes_file())
        likes = likes_reader.get_likes()

        log(u"{0} reações contabilizadas.".format(len(likes)))

        del likes_reader
        return likes
