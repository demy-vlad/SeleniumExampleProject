from typing import List
from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase



class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = 'body > div.mainmenu.ff-roboto > div > ul > li > a'
        self.__nav_header_lang_ua: str = 'div.header_lang > a:nth-child(3)'
        self.__nav_header_lang_ru: str = 'div.header_lang > a:nth-child(2)'
        self.__nav_catalog_title: str = 'body > div:nth-child(13) > div > div > span'
        self.CATALOG_TITLE: str = "Каталог товаров"
        self.NAV_LINK_TEXT_RU = "Гаджеты,Компьютеры,Фото, TV ,Аудио,Бытовая техника,Климат,Дом,Детские товары,Авто,Инструмент,Туризм,Спорт,Часы и украшения"
        self.NAV_LINK_TEXT_UA = "Гаджети,Комп'ютери,Фото, TV ,Аудіо,Побутова техніка,Клімат,Будинок,Дитячі товари,Авто,Інструмент,Туризм,Спорт,Годинники і прикраси"

    def get_nav_links(self) -> List[WebElement]:
        '''Return WebElements for nav links'''
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_header_lang_ua(self)-> WebElement:
        '''Return a header language UA WebElement'''
        return self.is_visible('css', self.__nav_header_lang_ua, 'Header Lang UA')

    def get_header_lang_ru(self)-> WebElement:
        '''Return a header language RU WebElement'''
        return self.is_visible('css', self.__nav_header_lang_ru, 'Header Lang RU')

    def get_nav_links_text_ru(self) -> str:
        '''Return all nav links text. Return format is a String with comma separated values'''
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return ','.join(nav_links_text)
    
    def get_nav_links_text_ua(self) -> str:
        '''Return all nav links text. Return format is a String with comma separated values'''
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return ','.join(nav_links_text)

    def get_nav_link_by_name(self, name: str) -> WebElement:
        '''Return a nav link WebElement, the input is a link's name'''
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)

    def get_nav_link_catalog_title(self) -> WebElement:
        '''Return WebElements for nav links'''
        return self.is_visible('css', self.__nav_catalog_title, 'Title Catalog Navigation Links')

    def get_nav_link_catalog_title_text(self) -> str:
        '''Return catalog title text. Return format is a String with value'''
        catalog_title = self.get_nav_link_catalog_title()
        catalog_title_text = self.get_text_from_webelement(catalog_title)
        return catalog_title_text
