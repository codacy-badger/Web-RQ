#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from core.logger import log


class PostInitializer(object):
    __web_driver: RemoteWebDriver
    __login: str
    __old_login: str

    __password: str
    __old_password: str

    __page_id: str
    __post_id: str
    __access_token: str = ""

    __text_html_object: None
    __data_ft_object: None
    __reactions_object = None
    __comments_object = None
    __shares_object = None

    __last_post: str = ""
    __save_path: str = ""

    @staticmethod
    def set_web_driver(web_driver: RemoteWebDriver):
        PostInitializer.__web_driver = web_driver
        return PostInitializer

    @staticmethod
    def get_web_driver() -> RemoteWebDriver:
        return PostInitializer.__web_driver

    @staticmethod
    def set_login(login: str):
        PostInitializer.__login = login
        return PostInitializer

    @staticmethod
    def get_login() -> str:
        return PostInitializer.__login

    @staticmethod
    def set_password(password: str):
        PostInitializer.__password = password
        return PostInitializer

    @staticmethod
    def get_password() -> str:
        return PostInitializer.__password

    @staticmethod
    def set_page_id(page_id: str):
        PostInitializer.__page_id = page_id
        return PostInitializer

    @staticmethod
    def get_page_id() -> str:
        return PostInitializer.__page_id

    @staticmethod
    def set_post_id(post_id: str):
        PostInitializer.__post_id = post_id
        return PostInitializer

    @staticmethod
    def get_post_id() -> str:
        return PostInitializer.__post_id

    @staticmethod
    def is_running_account() -> bool:
        return (PostInitializer.get_login() == PostInitializer.__old_login) and (
            PostInitializer.get_password() == PostInitializer.__old_password)

    @staticmethod
    def get_access_token() -> str:
        if not PostInitializer.__access_token or not PostInitializer.is_running_account():
            from modules.social_media.facebook.packages.rest_server_exploit.auth_login import AuthLogin

            PostInitializer.__access_token = AuthLogin(email=PostInitializer.get_login(),
                                                       password=PostInitializer.get_password()).get_access_token()

            PostInitializer.__old_login = PostInitializer.get_login()
            PostInitializer.__old_password = PostInitializer.get_password()

        return PostInitializer.__access_token

    @staticmethod
    def get_last_post() -> str:
        return PostInitializer.__last_post

    @staticmethod
    def is_running_post() -> bool:
        return PostInitializer.get_post_id() == PostInitializer.get_last_post()

    @staticmethod
    def get_save_path() -> str:

        if not PostInitializer.is_running_post() or not PostInitializer.__save_path:
            from os import getcwd, makedirs
            from time import time
            base_dir = getcwd()
            handler = str(PostInitializer.get_web_driver().current_window_handle)

            # Base / Output / Facebook / page_id / post_id / unix_time
            PostInitializer.__save_path = "{0}/output/facebook/{1}/{2}/{3}/{4}".format(base_dir,
                                                                                       PostInitializer.get_page_id(),
                                                                                       PostInitializer.get_post_id(),
                                                                                       handler,
                                                                                       str(time()))
            log(u'Todos os dados do post serão salvos em: {0}'.format(PostInitializer.__save_path))
            makedirs(PostInitializer.__save_path, exist_ok=True)
            PostInitializer.__last_post = PostInitializer.get_post_id()

        return PostInitializer.__save_path

    @staticmethod
    def start():

        from modules.social_media.facebook.actions.post.text_html import TextHTML
        from modules.social_media.facebook.actions.post.data_ft import PostDataFt
        from modules.social_media.facebook.actions.post.reactions import PostReactions
        from modules.social_media.facebook.actions.post.comments import PostComments
        from modules.social_media.facebook.actions.post.shares import PostShares

        PostInitializer.__text_html_object = TextHTML(PostInitializer).extract()
        PostInitializer.__data_ft_object = PostDataFt(PostInitializer).extract()
        PostInitializer.__reactions_object = PostReactions(PostInitializer).extract()
        PostInitializer.__comments_object = PostComments(PostInitializer).extract()
        PostInitializer.__shares_object = PostShares(PostInitializer).extract()

        return PostInitializer

    @staticmethod
    def get_response() -> dict:

        return {
            "text_html": PostInitializer.__text_html_object.get_html_text(),
            "data_ft": PostInitializer.__data_ft_object.get_data_ft_dict(),
            "reactions": PostInitializer.__reactions_object.get_reactions_list(),
            "comments": PostInitializer.__comments_object.get_comments(),
            "shared_posts": PostInitializer.__shares_object.get_shares()
        }
