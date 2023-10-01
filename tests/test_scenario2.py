"""Этот модуль содержит в себе тесты, реализующие второй сценарий тестового задания."""

from pages.sbiscontactspage import SbisContactsPage


def test_confirm_region():
    """Этот тест проверяет правильность определения региона на странице Контакты."""
    TARGET_REGION = "Свердловская область"
    contacts_page = SbisContactsPage()
    contacts_page.navigate_to_url()
    contacts_page.wait_for_page_reload()
    # провярет смену региона в элементе title
    assert get_region_from_title(contacts_page.get_title()) == TARGET_REGION
    contacts_page.close_browser()


def test_change_region():
    """Этот тест проверяет правильность определения региона. """
    TARGET_CITY = "Петропавловск-Камчатский"
    TARGET_REGION = "Камчатский край"
    TARGET_REGION_CODE = "41"
    contacts_page = SbisContactsPage()
    contacts_page.navigate_to_url()
    contacts_page.click_region_change_span()
    contacts_page.wait_for_region_change_panel()
    contacts_page.click_new_region()
    contacts_page.wait_for_region_change()
    current_url = contacts_page.get_current_url()
    # проверяет изменился ли URL сайта
    assert get_region_code(current_url) == TARGET_REGION_CODE
    # проверяет, изменился ли список партнёров путёмм проверки элемента город.
    assert contacts_page.get_city_content() == TARGET_CITY
    # провярет смену региона в элементе title
    assert get_region_from_title(contacts_page.get_title()) == TARGET_REGION
    contacts_page.close_browser()


def get_region_code(url: str):
    """Этот метод позволяет извлечь код региона из URL страницы контактов сайта СБИС. 
    В качестве аргументов он принимает строку, содержающую URL и возвращает строку с кодом региона (2 цифры)"""
    splitted_url = url.split("/")
    code = splitted_url[4].split("-")[0]
    return code


def get_region_from_title(title: str):
    """Эта функция возвращает название региона. 
    Она принимает строку title."""
    title_splitted = title.split(" ")
    region = title_splitted[3] + " " + title_splitted[4]
    return region
