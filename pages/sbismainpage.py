"""Этот модуль содержит в себе класс SbisMainPage, содержащий в себе элементы главной страницы сайта СБИС и методы для работы с ними. 
ВАЖНО! При изменениии URL страницы, необходимо обновить значение константы URL для корректной работы тестов."""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By 
from .base import BasePage 
from .exceptions import ElementNotFound

URL = "https://sbis.ru/"

class SbisMainPage(BasePage):
    """Этот класс содерижт в себе элементы и методы, относящиеся к главной странице СБИС"""
    
    def __init__(self): 
        """Этот метод инициализирует экземпляр класса. Он вызывает __init__ метод родительского класса BasePage и передаёт в него заданный URL"""
        super().__init__(url=URL)

    def get_contacts_button(self):
        """Этот метод находит кнопку 'контакты' на главыной странице сайта"""
        BUTTON_XPATH = "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a"
        try:
            return self.driver.find_element(By.XPATH, BUTTON_XPATH)
        except NoSuchElementException as exc:
            self.make_screenshot()
            raise ElementNotFound("Кнопка Контакты не найдена на странице") from exc
        except Exception as exc:
            self.make_screenshot()
            raise exc 
    
    def click_contacts_button(self):
        """Этот метод выполняет нажатие на кнопку контакты на главной странице сайта"""
        return self.get_contacts_button().click() 
    
        
    



    
    

