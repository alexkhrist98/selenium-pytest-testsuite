from selenium.webdriver.common.by import By 
from .base import BasePage 

URL = "https://sbis.ru/contacts/"

class SbisContactsPage(BasePage):
    """Этот класс описывает страницу контактов сайта СБИС"""

    def __init__(self):
        """Этот метод инициализирует экземпляр класса SbisContactsPage. 
        Он вызывает метод init класса BasePage и передаёт в него адрес страницы"""
        super().__init__(url=URL)

    def get_tensor_banner(self):
        """Этот метод возвращает элемент 'баннер ТЕНЗОР'. """
        BANNER_XPATH = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/a"
        return self.driver.find_element(By.XPATH, BANNER_XPATH)
    
    def click_tensor_banner(self): 
        """Этот метод отправляет действие клика на баннер ТЕНЗОР"""
        return self.get_tensor_banner().click() 
