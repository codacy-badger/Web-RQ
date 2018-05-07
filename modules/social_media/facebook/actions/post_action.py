#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import base64
import os
import time
from urllib import parse
import json
import codecs
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
import os.path
from core.logger import log
from modules.social_media.facebook.elements.post_elements import PostElements
from tools.file_download import FileDownload
from modules.social_media.facebook.book.post_book import PATTERN_PAGE_POST_REACTIONS
from modules.social_media.facebook.helper.likes_file_reader import LikesFileReader
from modules.social_media.facebook.packages.rest_server_exploit.auth_login import AuthLogin


"""
@deprecated
"""

class Post:
    """
    Classe para captura de dados em postagem
    """

    # Instancia
    __web_driver: RemoteWebDriver = None

    # Id da pagina
    __page_id: str

    # Id do post
    __post_id: str

    # Path em que os dados serao salvos
    __save_path: str

    # Data ft
    __data_ft_file: str

    # Text HTML
    __text_html_file: str

    # Video
    __video_file: str

    # Vide b64
    __video_b64_file: str

    # Likes List
    __likes_list: list = []

    # Likes html file
    __likes_html_file: str

    # User login
    __user_login = ""

    # User password
    __user_password = ""

    # Access Token
    __access_token = ""

    @staticmethod
    def set_user_login(login: str):
        Post.__user_login = login
        return Post

    @staticmethod
    def get_user_login() -> str:
        return Post.__user_login

    @staticmethod
    def set_user_password(password: str):
        Post.__user_password = password
        return Post

    @staticmethod
    def get_user_password():
        return Post.__user_password

    @staticmethod
    def get_access_token():

        if not Post.__access_token:
            Post.__access_token = AuthLogin(email=Post.get_user_login(), password=Post.get_user_password()).get_access_token()

        return Post.__access_token

    @staticmethod
    def set_page_id(page_id: str):
        Post.__page_id = page_id
        return Post

    @staticmethod
    def get_page_id() -> str:
        return Post.__page_id

    @staticmethod
    def set_post_id(post_id: str):
        Post.__post_id = post_id
        return Post

    @staticmethod
    def get_post_id() -> str:
        return Post.__post_id

    @staticmethod
    def set_web_driver(web_driver: RemoteWebDriver):
        Post.__web_driver = web_driver
        return Post

    @staticmethod
    def get_web_driver() -> RemoteWebDriver:
        return Post.__web_driver

    @staticmethod
    def set_save_path(save_path: str):
        Post.__save_path = save_path
        return Post

    @staticmethod
    def post_capture(web_driver: RemoteWebDriver, page_id: str, post_id: str):

        """

        Inicia captura da postagem
        :param web_driver: RemoteWebDriver
        :param page_id: str
        :param post_id: str
        :return: None

        """

        Post.set_page_id(page_id).set_post_id(post_id).set_web_driver(web_driver).set_save_path(Post.__get_handle_dir())

        Post.__save_post_data()
        return Post

    @staticmethod
    def __get_handle_dir() -> str:

        """

        Prepara o path onde os dados serao salvos
        :return: str

        """

        # Script base path
        base_dir = os.getcwd()

        # Browser Handler
        handler = str(Post.__web_driver.current_window_handle)

        # Base / Output / Facebook / page_id / post_id / unix_time
        path = "{0}/output/facebook/{1}/{2}/{3}/{4}".format(base_dir, Post.__page_id, Post.__post_id, handler,
                                                            str(time.time()))

        log(u'Todos os dados do post serão salvos em: {0}'.format(path))

        os.makedirs(path, exist_ok=True)

        return path

    @staticmethod
    def __save_post_data():

        """

        Caminhos do Crawler
        :return: None

        """

        Post.__get_base_data().__get_text_html().__get_video().__get_reactions()

    @staticmethod
    def set_data_ft_file(data_ft: str):
        Post.__data_ft_file = data_ft
        return Post

    @staticmethod
    def get_data_ft_file() -> str:
        return Post.__data_ft_file

    @staticmethod
    def set_text_html_file(text_html_file: str):
        Post.__text_html_file = text_html_file
        return Post

    @staticmethod
    def get_text_html_file() -> str:
        return str(Post.__text_html_file)

    @staticmethod
    def set_video_file(video_file: str):
        Post.__video_file = video_file
        return Post

    @staticmethod
    def get_video_file() -> str:
        return Post.__video_file

    @staticmethod
    def set_video_file_b64(video_file: str):
        Post.__video_b64_file = video_file
        return Post

    @staticmethod
    def get_video_file_b64() -> str:
        return Post.__video_b64_file

    @staticmethod
    def set_likes_file(likes_file: str):
        Post.__likes_html_file = likes_file
        return Post

    @staticmethod
    def get_likes_file() -> str:
        return Post.__likes_html_file

    @staticmethod
    def __get_base_data():

        """

        Obtem dados base do Post
        :return: Post

        """

        driver = Post.get_web_driver()

        log(u"Obtendo dados base do post.")

        element = PostElements.get_post_data(driver)

        data_ft = ""

        if element:
            data_ft = element.get_attribute('data-ft')
            Post.set_data_ft_file(Post.__save_path + '/data-ft.json')

        if data_ft:

            with codecs.open(Post.get_data_ft_file(), mode='w', encoding="utf-8") as f:
                f.write(data_ft)

            log(u"Dados base salvos em: [{}]".format(Post.get_data_ft_file()))

        return Post

    @staticmethod
    def __get_text_html():

        """
        Obtem texto html do post
        :return: Post
        """

        log(u"Obtendo texto html do post.")

        element = PostElements.get_post_text_html(Post.get_web_driver())

        html = ""

        if element:
            html = element.get_attribute('innerHTML')

        Post.set_text_html_file(Post.__save_path + '/text.html')

        with codecs.open(Post.get_text_html_file(), 'w', encoding="utf-8") as f:
            f.write(html)

        log(u"Texto HTML salvo em: [{}]".format(Post.get_text_html_file()))

        return Post

    @staticmethod
    def __get_video():

        """
        Obtem o video no post (se existir)
        :return: Post
        """

        # Se o video existe
        log(u"Verificando existência de vídeo no POST.")

        video = PostElements.get_post_video(driver=Post.get_web_driver())

        if video:
            log("Foi encontrado um video no post.")

            # Url with redirect
            url = video.get_attribute('href')

            # Params
            params = dict(parse.parse_qs(parse.urlsplit(url).query))

            # Url do video
            video_url = params['src'][0]

            extension = FileDownload.get_format(video_url)

            # Target file
            Post.set_video_file(Post.__save_path + "/video.{0}".format(extension))

            # B64 target file
            Post.set_video_file_b64(Post.__save_path + "/video.{0}.{1}".format(extension, 'b64'))

            # Download
            FileDownload.download(video_url, Post.get_video_file())

            # Convert
            with open(Post.get_video_file(), 'rb') as video:
                # To BASE64
                video_encode = base64.encodebytes(video.read())

                with open(Post.get_video_file_b64(), 'wb') as b64video:
                    b64video.write(video_encode)

            log("Video salvo em: [{}]".format(Post.__video_file))
            log("Video base64 salvo em: [{}]".format(Post.__video_b64_file))

        return Post

    @staticmethod
    def __insert_like(reaction: str, username: str, user_url: str):
        data = {
            # "id": Profile.getId(user_url),
            "name": username,
            "profile_url": user_url,
            "reaction": reaction
        }

        log("Identificado: ")
        log(json.dumps(data, indent=4))

        Post.__likes_list.append(data)

    @staticmethod
    def __get_likes_list() -> list:
        return Post.__likes_list

    @staticmethod
    def __get_reactions(in_extended: bool = False):

        if not in_extended:
            log(u"Obtendo reações extendidas...")
            Post.get_web_driver().get(PATTERN_PAGE_POST_REACTIONS.format(Post.get_post_id()))

        lines = PostElements.get_post_reactions_lines(Post.get_web_driver())

        lines_count = len(lines)

        if not in_extended and lines_count > 0:
            log(u"Lendo reações...")

            more = str(lines[lines_count - 1].find_element_by_tag_name("a").get_attribute("href")).replace(
                "limit=10", "limit=1000000")

            Post.get_web_driver().get(more)
            Post.__get_reactions(True)

        if lines_count > 0 and in_extended:
            log(u"Salvando reações")

            Post.set_likes_file(Post.__save_path + '/likes.html')
            file_path = Post.get_likes_file()

            with codecs.open(file_path, "w", encoding="utf-8") as infile:
                page_source = Post.get_web_driver().page_source
                infile.write(page_source)

            log(u"Reações salvas em: [{0}]".format(file_path))

    @staticmethod
    def get_data_ft() -> dict:
        dict_ret = {}

        if os.path.isfile(Post.get_data_ft_file()):
            dict_ret = json.load(codecs.open(Post.get_data_ft_file(), "r", encoding="utf-8"))

        return dict_ret

    @staticmethod
    def get_text_html() -> str:
        html = ""

        if os.path.isfile(Post.get_text_html_file()):
            with codecs.open(Post.get_text_html_file(), "r", encoding="utf-8") as f:
                html = f.read()

        return html

    @staticmethod
    def get_video_b64() -> bytes:
        b = None

        if os.path.isfile(Post.get_video_file_b64()):
            with open(Post.get_video_file_b64(), 'wb') as base64video:
                b = base64video.read()

        return b

    @staticmethod
    def get_likes() -> list:
        file = Post.get_likes_file()
        likes_reader = LikesFileReader(Post.get_likes_file())
        likes = likes_reader.get_likes()
        del likes_reader
        return likes

    @staticmethod
    def get_post_comments() -> dict:
        post = Post.get_post_id()
        page = Post.get_page_id()
        access_token = Post.get_access_token()

        from modules.social_media.facebook.packages.facebook_api.post_comments import PostComments
        comments = PostComments(access_token=access_token, page_id=page, post_id=post)

        return comments.get_response()

    @staticmethod
    def get_response() -> dict:

        data = {
            "data-ft": Post.get_data_ft(),
            "post-text-html": Post.get_text_html(),
            "likes": Post.get_likes(),
            "comments": Post.get_post_comments()
        }

        return data
