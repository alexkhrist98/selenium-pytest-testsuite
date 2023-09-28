import time 
from pages.sbismainpage import SbisMainPage
from pages.sbiscontactspage import SbisContactsPage  
from pages.tensormainpage import TensorMainPage 

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
    contacts_page = SbisContactsPage() 
    contacts_page.navigate_to_url() 
    contacts_page.click_tensor_banner() 
    contacts_page.switch_tab()
    assert contacts_page.get_current_url() == TARGET_URL #проверяет переход на сайт компании ТЕНЗОР
    contacts_page.close_browser()

def test_power_in_people_block_present(): 
    """Этот тест проверяет наличие блока Сила в людях на главной странице сайта."""
    main_page = TensorMainPage()
    main_page.navigate_to_url()
    main_page.scroll_down_with_keyboard()
    time.sleep(10)
    assert main_page.get_power_in_people_block() #проверяет наличие блока сила в людях на странице
    main_page.close_browser() 

