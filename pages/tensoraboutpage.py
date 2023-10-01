"""Этот модуль содержит в себе класс TensorMainPage, описывающий страницу О компании на сайте ТЕНЗОР. 
Класс TensorAboutPage предназначен для отражение элементов страницы в коде без необходимости работать с методами
selenium webdriver. 
ВАЖНО! При изменении URL страницы, необходимо задать новое значение константы URL в этом модуле для корректной работы тестов."""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import BasePage
from .exceptions import ElementNotFound

URL = "https://tensor.ru/about/"


class TensorAboutPage(BasePage):
    """Этот класс описывает страницу о компании на сайте Тензор. Он наследует часть методов из класса BasePage. """

    def __init__(self):
        """Этот метод инициализирует экземпляр класса TensorAboutPage. 
        Метод вызывает __init__ метод родительского класса и передаёт в него указанный в файле tensoraboutpage.py адрес страницы."""
        super().__init__(url=URL)

    def get_working_block(self):
        """Этот метод позволяет найти блок Работаем на странице. Он возвращает элемент, содержащий указанный блок. """
        BLOCK_XPATH = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]"
        try:
            return self.driver.find_element(By.XPATH, BLOCK_XPATH)
        except NoSuchElementException as exc:  # отрабатывает ненахождение элемента по его XPATH
            self.make_screenshot()
            raise ElementNotFound("Блок Работаем не обнаружен") from exc
        except Exception as unexpected_exception:  # обрабатывает непредусмотренные исключения
            self.make_screenshot()
            raise unexpected_exception

    def scroll_working_block_into_view(self):
        """Этот метод позволяет прокрутить страницу и вывести блок Работаем на экран. """
        return ActionChains(self.driver).scroll_to_element(self.get_working_block()).perform()

    def get_images_from_working_block(self):
        """Этот метод возвращает картинки, расположенные в блоке Работаем. """
        IMAGES_TAG_NAME = "img"
        try:
            images = self.get_working_block().find_elements(By.TAG_NAME, IMAGES_TAG_NAME)
        except Exception as unexpected_exception:
            self.make_screenshot()
            raise unexpected_exception
        if images:
            return images
        else:
            self.make_screenshot()
            raise ElementNotFound("Картинки в блоке Работаем не найдены")

    def get_images_width(self):
        """Этот метод получает значения width у картинок в блоке Работаем."""
        width_list = []
        images = self.get_images_from_working_block()
        for image in images:
            width = image.get_attribute("width")
            width_list.append(width)
        # возвращает список, содержащий значения ширине у всех картинок блока Работаем
        return width_list

    def get_images_heights(self):
        """Этот метод позволяет получить данные о высоте картинок внутри блока Работаем на странице. 
        Метод возвращает список числовых значений высот картинок."""
        heights_list = []
        images = self.get_images_from_working_block()
        for image in images:
            height = image.get_attribute("height")
            heights_list.append(height)
        return heights_list
