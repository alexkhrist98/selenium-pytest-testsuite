from abc import ABC
from datetime import datetime 
import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 

class BasePage(ABC):
    """Этот абстрактный класс создаёт необходимые базовые методы для работы с тестируемой страницей. 
    Для работы с новой страницей, необходимо отнаследоваться от этого класса и расширить его поведение дополнительными методами 
    подкласса."""

    def __init__(self, url: str):
        """Этот метод создаёт экземпляр класса веб-страница. В качесте аргументов он принимает адрес страницы. 
        Он также инициализирует свойство self.driver, присваевая ему экземпляр класса webdriver.Chrome
        Также этот метод инициализирует опции веб-драйвера, в частности, местоположение скриншотов, которые
        сохраняются при возникновнеии исключений."""
        screenshot_dir = self._make_screenshot_dir()
        driver_options = webdriver.ChromeOptions() 
        driver_options.add_argument(f"--screenshot-dir={screenshot_dir}")
        self.driver = webdriver.Chrome(options=driver_options) 
        self.url = url 
    
    @staticmethod
    def _make_screenshot_dir():
        """Этот статический метод создаёт папку, в которой будут храниться скриншоты, 
        сохраняемые драйвером во врмея проведения тестов."""
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        return screenshot_dir


    def navigate_to_url(self):
        """ЭЭтот метод вызывает метод webdriver.get и передаёт ему аргумент self.url"""
        return self.driver.get(self.url)

    def scroll_down(self, offset: int): 
        """Этот метод позволяет прокрутить страницу вниз на определённое количетсво пикселей. 
        В качестве аргумента он принимает offset - количество пикселей.
        ВНИМАНИЕ! Метод был переписан по причине невозможности выполнения JavaScript на сайте.
        Для прокрутки к конкретном элементу, используйте методы, определённыевнутри подклассов страниц."""
        return ActionChains(self.driver).scroll_by_amount(0, offset).perform()

    def scroll_up(self, offset: int = 0): 
        """Этот метод позволяет прокрутить страницу вверх на заданное количетсво пикселей.
        Он принимает аргумент offset - количество пикселей. 
        Для прокрутки к конкретному элементу, используйте методы, определённые в подклассах."""
        return ActionChains(self.driver).scroll_by_amount(0, -offset).perform()

    def go_back(self):
        """Этот метод позволяет вернуться на одну страницу назад."""
        return self.driver.back() 
    def get_current_url(self): 
        """Этот метод возвращается адрес страницы, на которой находится драйвер в момент вызова этого метода"""
        return self.driver.current_url

    def switch_tab(self, tab_number: int = 1): 
        """Этот метод позволяет переключаться между вкладками окна драйвера. 
        В качестве аргумента он принимает номер вкладки. По умолчанию метод переключает на следующую вкладку.
        Индексация вкладок выглдяти так:
        -Под индексом 0 обозначена текущая вкладка. 
        -Под индексом 1 - следующаяю 
        -Под индексом -1 - предыдущая."""
        return self.driver.switch_to.window(self.driver.window_handles[tab_number])
    
    def close_browser(self): 
        """Этот метод позволяет закрыть браузер после завершения теста"""
        return self.driver.close() 
    
    def make_screenshot(self): 
        """Этот метод созраняет скриншот страницы. 
        Он будет использован при обработке исключений для сохранения информации о том, что произошло"""
        return self.driver.save_screenshot(self._make_screenshot_dir() + f"\\{self.__class__.__name__}: {datetime.now()}.png")

    def __str__(self):
        """Этот метод возвращает строку с используемым адресом страницы"""
        return f"{self.__class__.__name__}({self.url})"
        

        
