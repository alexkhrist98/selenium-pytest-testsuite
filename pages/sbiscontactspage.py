"""Этот модуль содержит в себе класс SbisContactsPage, содержащий в себе элементы  страницы контактов сайта СБИС и методы для работы с ними. 
ВАЖНО! При изменениии URL страницы, необходимо обновить значение константы URL для корректной работы тестов."""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .base import BasePage
from .exceptions import ElementNotFound

URL = "https://sbis.ru/contacts/"


class SbisContactsPage(BasePage):
    """Этот класс описывает страницу контактов сайта СБИС"""

    def __init__(self):
        """Этот метод инициализирует экземпляр класса SbisContactsPage. 
        Он вызывает метод init класса BasePage и передаёт в него адрес страницы"""
        super().__init__(url=URL)

    def get_tensor_banner(self):
        """Этот метод возвращает элемент 'баннер ТЕНЗОР'. """
        BANNER_XPATH = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/a/img"
        try:
            return self.driver.find_element(By.XPATH, BANNER_XPATH)
        except NoSuchElementException as exc:
            self.make_screenshot()
            raise ElementNotFound("Баннер Тензор не найден") from exc
        except Exception as e:
            self.make_screenshot()
            raise e

    def click_tensor_banner(self):
        """Этот метод отправляет действие клика на баннер ТЕНЗОР"""
        return self.get_tensor_banner().click()

    def get_region_change_span(self):
        """Этот метод позволяет найти на странице ссылку, вызывающую экран смены региона."""
        SPAN_XPATH = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span"
        try:
            return self.driver.find_element(By.XPATH, SPAN_XPATH)
        except NoSuchElementException as exc:
            self.make_screenshot()
            raise ElementNotFound(
                "Кнопка смены региона не обнаружена") from exc
        except Exception as exc:
            self.make_screenshot()
            raise exc

    def click_region_change_span(self):
        """Этот метод позволяет нажать на элемент смены региона на странице."""
        return self.get_region_change_span().click()

    def get_new_region(self):
        """Этот метод позволяет выделить на странице элемент, соответсвующий желаемумо региону в блоке смены региона. 
        На данный момент новый регион - Камчатский край. 
        Для изменения поведения метода, необходимо изменить значение REGION_XPATH, подставив туда полный путь к новому элементу"""
        REGION_XPATH = "/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div/ul/li[43]/span"
        try:
            return self.driver.find_element(By.XPATH, REGION_XPATH)
        except NoSuchElementException as exc:
            self.make_screenshot()
            raise ElementNotFound(
                "Элемент Камчатский край не обнаружен") from exc
        except Exception as exc:
            self.make_screenshot()
            raise exc

    def click_new_region(self):
        """Этот метод позволяет нажать на элемент, отвечающий за смены региона на выбранный."""
        return self.get_new_region().click()

    def wait_for_region_change_panel(self):
        """Этот метод позволяет дождаться загрузки панели выбора региона."""
        delay = WebDriverWait(self.driver, 10)
        PANEL_CLASS_NAME = "sbis_ru-Region-Panel"
        return delay.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, PANEL_CLASS_NAME)))

    def wait_for_region_change(self):
        """Этот метод позволяет дождаться появления строки региона на странице."""
        delay = WebDriverWait(self.driver, 10)
        return delay.until(expected_conditions.url_changes(self.get_current_url()))

    def get_contacts_list(self):
        """Этот метод возвращает список партнёров в разеделе контакты на сайте СБИС. """
        LIST_XPATH = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[3]"
        try:
            return self.driver.find_element(By.XPATH, LIST_XPATH)
        except NoSuchElementException as exc:
            self.make_screenshot()
            raise ElementNotFound("Список контактов не обнаружен") from exc
        except Exception as unexpected_exception:
            self.make_screenshot()
            raise unexpected_exception

    def get_city_from_partners(self):
        """Этот метод возвращает город из списка партнёров на странице."""
        CITY_CLASS_NAME = "sbisru-Contacts-City__item-name"
        try:
            return self.get_contacts_list().find_element(By.CLASS_NAME, CITY_CLASS_NAME)
        except NoSuchElementException as exc:
            self.make_screenshot()
            raise ElementNotFound(
                "Элемент город в списке партнёров не обнаружен") from exc
        except Exception as e:
            self.make_screenshot()
            raise e

    def get_city_content(self):
        """Этот метод возвращает строку, содержающую контент элемента город."""
        return self.get_city_from_partners().text
