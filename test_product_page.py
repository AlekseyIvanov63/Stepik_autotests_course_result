from pages.product_page import ProductPage


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


def test_guest_should_see_product_link(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()


def test_guest_should_add_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
