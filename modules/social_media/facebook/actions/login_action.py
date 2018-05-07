#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from core.driver_utils import check_exists_by_xpath
from core.logger import log
from modules.social_media.facebook.book.login_book import XPATH_INPUT_LOGIN, XPATH_INPUT_PASSWORD, XPATH_INPUT_SUBMIT, \
    XPATH_SEARCH
from modules.social_media.facebook.configs.consts import FACEBOOK_LOGIN_URL, FACEBOOK_CANCEL_SAVE_DEVICE, \
    FACEBOOK_PHONE_SKIP, FACEBOOK_SEARCH_SKIP, FACEBOOK_SAVE_DEVICE_CHECK, FACEBOOK_BLOCK_OR_CHEKCPOIN_CHECK, \
    FACEBOOK_ACCOUNT_START_CHECK, FACEBOOK_STEP_SEARCH_CHECK


class LoginException(Exception):
    pass


class Login:
    """
    Classe para realizar login em um browser
    """

    # Instancia
    __web_driver: RemoteWebDriver = None

    # Login (text-plain)
    __login: str = ''

    # Password (text-plain)
    __password: str = ''

    @staticmethod
    def set_web_driver(web_driver: RemoteWebDriver):
        Login.__web_driver = web_driver
        return Login

    @staticmethod
    def get_web_driver() -> RemoteWebDriver:
        return Login.__web_driver

    @staticmethod
    def set_login(login: str):
        Login.__login = login
        return Login

    @staticmethod
    def get_login() -> str:
        return Login.__login

    @staticmethod
    def set_password(password: str):
        Login.__password = password
        return Login

    @staticmethod
    def get_password() -> str:
        return Login.__password

    @staticmethod
    def facebook_login(web_driver: RemoteWebDriver, login: str, password: str) -> bool:

        """
        Funcao para realizar os passos necessarios para o login, e retornar se foi bem sucedida ou nao
        :param web_driver: RemoteWebDriver instancia do driver
        :param login: str login text-plain
        :param password: str senha text-plain
        :return: bool login realizado com sucesso?
        """

        # Salvamos a instancia
        Login.set_web_driver(web_driver)

        # Salvamos o login
        Login.set_login(login)

        # Salvamos a senha
        Login.set_password(password)

        # Acessamos a pagina de login
        Login.__access()

        # Informamos o Handler
        log('Handler: [{}]'.format(web_driver.current_window_handle))

        # Processos para o login
        is_logged = Login.__input_login().__input_password().__submit().__check_save_device().__is_logged()

        if is_logged:
            log("O login foi realizado com sucesso!")

        return is_logged

    @staticmethod
    def __input_login():

        """
        Funcao para preencher o input de login.
        :return: Login
        """

        if check_exists_by_xpath(Login.get_web_driver(), XPATH_INPUT_LOGIN):
            Login.get_web_driver().find_element_by_xpath(XPATH_INPUT_LOGIN).send_keys(Login.get_login())

        return Login

    @staticmethod
    def __input_password():

        """
        Funcao para preencher o input de senha.
        :return: Login
        """

        if check_exists_by_xpath(Login.get_web_driver(), XPATH_INPUT_PASSWORD):
            Login.get_web_driver().find_element_by_xpath(XPATH_INPUT_PASSWORD).send_keys(Login.get_password())

        return Login

    @staticmethod
    def __submit():

        """
        Funcao para realizar submit/login
        :return: Login
        """

        if check_exists_by_xpath(Login.get_web_driver(), XPATH_INPUT_SUBMIT):
            Login.get_web_driver().find_element_by_xpath(XPATH_INPUT_SUBMIT).click()

        return Login

    @staticmethod
    def __check_save_device():
        """
        Checa se o Facebook pediu para salvar o dispositivo.
        :return: Logn
        """
        log('Verificando se estamos no passo para salvar dispositivos.')

        current_url = Login.get_web_driver().current_url

        if FACEBOOK_SAVE_DEVICE_CHECK in current_url:

            log(u'O Facebook pediu para salvar o dispositivo, por padrao estamos negando.')
            Login.get_web_driver().get(FACEBOOK_CANCEL_SAVE_DEVICE)

        elif FACEBOOK_BLOCK_OR_CHEKCPOIN_CHECK in current_url:

            Login.get_web_driver().delete_all_cookies()
            Login.get_web_driver().get(FACEBOOK_LOGIN_URL)

            raise LoginException('Conta bloqueada, por favor verifique.')

        elif FACEBOOK_ACCOUNT_START_CHECK in current_url:

            log('Passando por passos iniciais...')

            if FACEBOOK_STEP_SEARCH_CHECK in current_url:

                Login.get_web_driver().get(FACEBOOK_SEARCH_SKIP)

            else:

                Login.get_web_driver().get(FACEBOOK_PHONE_SKIP)

            Login.__check_save_device()

        return Login

    @staticmethod
    def __access():

        """
        Funcao para acessar a pagina de Login do Facebook
        :return: Login
        """

        Login.__web_driver.get(FACEBOOK_LOGIN_URL)

        return Login

    @staticmethod
    def __is_logged() -> bool:
        """
        Funcao para verificar se o usuario esta logado
        :return: bool
        """
        return check_exists_by_xpath(Login.__web_driver, XPATH_SEARCH)
