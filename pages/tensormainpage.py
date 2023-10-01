"""Этот модуль содержит в себе класс TensorMainPage. 
В классе заключены методы и элементы главной страницы сайта компании ТЕНЗОР.
Этот класс позволяет работать с элементами страницы, не взаимодействуя с методами selenium webdriver"""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait  
from .base import BasePage 
from .exceptions import ElementNotFound

URL = "https://tensor.ru/"

class TensorMainPage(BasePage): 
    """Этот класс описывает главную страницу сайта компании Тензор и элементы этой страницы, необходимые для дестирования."""

    def __init__(self): 
        """Этот метод инициализирует экземпляр класса TensorMainPage. 
        Он вызывает __init__ метод класса BasePage и передаёт в него адрес страницы"""
        super().__init__(url=URL)
    
    def get_power_in_people_block(self): 
        """Этот метод возвращает элемент 'блок Сила в людях'."""
        BLOCK_XPATH = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div"
        try:
            return self.driver.find_element(By.XPATH, BLOCK_XPATH)
        except NoSuchElementException as exc:
            self.make_screenshot()
            self.close_browser()
            raise ElementNotFound("Блок Сила в людях не обнаружен на странице") from exc
        except Exception as exc:
            self.make_screenshot()
            raise exc
    
    def get_more_link(self):
        """Этот метод находит ссылку Подробнее в блоке Сила в людях. Метод возвращает элемент, содержащий в себе эту ссылку"""
        LINK_XPATH = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a"
        try:
            return self.get_power_in_people_block().find_element(By.XPATH, LINK_XPATH)
        except NoSuchElementException as exc:
            self.make_screenshot()
            self.close_browser()
            raise ElementNotFound("Ссылка подробнее не найдне") from exc
        except Exception as exc:
            self.make_screenshot()
            self.close_browser()
            raise exc
        
    def scroll_power_in_people_into_view(self): 
        """Этот метод использует ActionChains для того, чтобы прокрутить окно браузера к элементу Блок Сила в людях."""
        try:
            return ActionChains(self.driver).scroll_to_element(self.get_power_in_people_block()).perform()
        except Exception as e: 
            self.make_screenshot()
            raise e 
    
    def wait_for_more_link_visible(self): 
        """Этот метод позволяет дождаться, пока ссылка подробнее в блоке Сила в людях не появится в зоне видимости."""
        delay = WebDriverWait(self.driver, 10)
        return delay.until(expected_conditions.visibility_of(self.get_more_link()))

    def click_more_link(self):
        """Этот метод нажимает на ссылку Подробнее в блоке Сила в людях"""
        try: 
            return self.get_more_link().click() 
        except Exception as e: 
            self.make_screenshot()
            raise e 

    