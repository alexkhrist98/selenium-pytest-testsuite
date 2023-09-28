from pages.sbismainpage import SbisMainPage
from pages.sbiscontactspage import SbisContactsPage  

def test_sbis_go_to_contacts(): 
    """Этот тест проверяет переход на страницу контакты с главной страницы СБИС"""
    page = SbisMainPage() 
    page.navigate_to_url() 
    page.click_contacts_button() 
    assert page.get_current_url() == page.url + "contacts"
