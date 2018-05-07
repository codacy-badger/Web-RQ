#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from modules.social_media.facebook.actions.post.initializer import PostInitializer
from core.logger import log


class PostComments(PostInitializer):
    __comments: None

    def __init__(self,shadow_class: PostInitializer):
        PostComments = shadow_class

    def extract(self):
        log(u"Extraindo comentários...")
        from modules.social_media.facebook.packages.facebook_api.post_comments import PostComments as Comments

        self.__comments = Comments(access_token=PostComments.get_access_token(), page_id=PostComments.get_page_id(),
                                       post_id=PostComments.get_post_id())
        return self

    def get_comments(self) -> list:
        comments = self.__comments.get_response()

        log(u"{0} comentários foram extraidos.".format(len(comments)))

        return comments
