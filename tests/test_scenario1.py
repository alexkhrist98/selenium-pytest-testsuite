import time 
from pages.sbismainpage import SbisMainPage
from pages.sbiscontactspage import SbisContactsPage  
from pages.tensormainpage import TensorMainPage 
from pages.tensoraboutpage import TensorAboutPage 

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
    assert main_page.get_power_in_people_block() #проверяет наличие блока сила в людях на странице
    main_page.close_browser()

def test_more_link_in_power_of_people():
    """Этот тест проверяет корректность перехода по ссылке в блоке Сила в людях"""
    TARGET_URL = "https://tensor.ru/about"
    main_page = TensorMainPage() 
    main_page.navigate_to_url() 
    main_page.scroll_power_in_people_into_view() 
    main_page.click_more_link() 
    assert main_page.get_current_url() == TARGET_URL #проверяет правильность перехода по ссылке
    main_page.close_browser() 

def test_check_image_size_in_working_block():
    """Этот тест проверяет, совпадают ли высоты и ширина у картинок в разделе Работаем 
    страница О компании на сайте Тензо."""
    about_page = TensorAboutPage() 
    about_page.navigate_to_url() 
    about_page.scroll_working_block_into_view()
    heights_list = about_page.get_images_heights() 
    widths_list = about_page.get_images_width()
    assert size_isequal(heights_list, widths_list) == True #проверяет, совпадают ли длина и ширина изображений в блоке Работаем
    about_page.close_browser() 

def size_isequal(heights: list, widths: list): 
    """Эта функция проверяет, совпадают ли высота и ширина элементов в блоке Работаем. 
    В качестве аргументов он принимает списки, содержащие значения высоты и ширины для каждого изображения (список widths и список hights).
    Метод возвращает True, если значения совпадают. Если же хоть одно значение не совпадает, он возвращает False."""
    height_pivot = heights[0]
    width_pivot = widths[0]
    for height, width in zip(heights, widths):
        if height != height_pivot or width != width_pivot: 
            return False 
    return True
        



