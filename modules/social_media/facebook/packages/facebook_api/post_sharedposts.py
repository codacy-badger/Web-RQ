#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
class PostSharedPosts(object):
    from modules.social_media.facebook.configs.consts import FACEBOOK_API_VERSION
    __page_id = ""
    __post_id = ""
    __access_token = ""

    __API_VERSION = FACEBOOK_API_VERSION

    def __init__(self, access_token: str = "", page_id: str = "", post_id: str = ""):
        self.set_access_token(access_token=access_token).set_page_id(page_id).set_post_id(post_id)

    def set_access_token(self, access_token: str):
        self.__access_token = access_token
        return self

    def get_access_token(self) -> str:
        return self.__access_token

    def set_post_id(self, post_id: str):
        self.__post_id = post_id
        return self

    def get_post_id(self) -> str:
        return self.__post_id

    def get_page_id(self) -> str:
        return self.__page_id

    def set_page_id(self, page_id: str):
        self.__page_id = page_id
        return self

    def get_response(self) -> list:
        from facebook import GraphAPI
        graph = GraphAPI(access_token=self.get_access_token(), version=self.__API_VERSION)

        return list(graph.get_all_connections(id="{0}_{1}".format(self.get_page_id(), self.get_post_id()),
                                              connection_name="sharedposts?fields=created_time,message,story,id,parent_id,from"))
