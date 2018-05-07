#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from modules.social_media.facebook.actions.post.initializer import PostInitializer
from core.logger import log


class PostShares(PostInitializer):
    __shared_posts: None

    def __init__(self, shadow_class: PostInitializer):
        PostShares = shadow_class

    def extract(self):
        log(u"Extraindo compartilhamentos...")
        from modules.social_media.facebook.packages.facebook_api.post_sharedposts import PostSharedPosts

        self.__shared_posts = PostSharedPosts(access_token=PostShares.get_access_token(), page_id=PostShares.get_page_id(),
                                   post_id=PostShares.get_post_id())
        return self

    def get_shares(self) -> list:
        shares = self.__shared_posts.get_response()

        log(u"{0} compartilhamentos foram extraidos.".format(len(shares)))

        return shares
