from pages.sbismainpage import SbisMainPage, URL  

def test_sbis_contacts(): 
    """Этот тест проверяет переход на страницу контакты с главной страницы СБИС"""
    page = SbisMainPage() 
    page.navigate_to_url() 
    page.click_contacts_button() 
    assert page.get_current_url() == URL + "contacts"