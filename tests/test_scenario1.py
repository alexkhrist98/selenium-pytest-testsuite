from pages.sbismainpage import SbisMainPage
from pages.sbiscontactspage import SbisContactsPage  
import time 

def test_sbis_go_to_contacts(): 
    """Этот тест проверяет переход на страницу контакты с главной страницы СБИС"""
    page = SbisMainPage() 
    page.navigate_to_url() 
    page.click_contacts_button() 
    assert page.get_current_url() == page.url + "contacts" #проверяет верность URL, на который переводит кнопка Контакты
    page.close_browser()

def test_contacts_go_to_tensor():
    """Этот тест проверяет переход на сайт компании Тензор путём клика по баннеру Тензор в разделе Контакты"""
    TARGET_URL = "https://tensor.ru/"
    page = SbisContactsPage() 
    page.navigate_to_url() 
    page.click_tensor_banner() 
    page.switch_tab()
    assert page.get_current_url() == TARGET_URL #проверяет переход на сайт компании ТЕНЗОР
    page.close_browser()
