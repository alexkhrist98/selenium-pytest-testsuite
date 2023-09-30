from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By 
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
        except NoSuchElementException:
            self.make_screenshot()
            self.close_browser()
            raise ElementNotFound("Блок Сила в людях не обнаружен на странице")
    
    def get_more_link(self):
        """Этот метод находит ссылку Подробнее в блоке Сила в людях. Метод возвращает элемент, содержащий в себе эту ссылку"""
        LINK_XPATH = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a"
        try:
            return self.get_power_in_people_block().find_element(By.XPATH, LINK_XPATH)
        except NoSuchElementException:
            self.make_screenshot()
            self.close_browser()
            raise ElementNotFound("Ссылка подробнее не найдне")
        except exception as e:
            self.make_screenshot()
            self.close_browser()
            raise e 
    
    def click_more_link(self):
        """Этот метод нажимает на ссылку Подробнее в блоке Сила в людях"""
        try: 
            return self.get_more_link().click() 
        except Exception as e: 
            self.make_screenshot()
            raise e 

    