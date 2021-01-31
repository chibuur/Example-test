from pages.main_page import MainPage
from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('number', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason = ' ')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = MainPage(browser, link)
    page.open()
    page_add = ProductPage(browser, link)
    page_add.add_to_basket()
    page.solve_quiz_and_get_code()
    page_add.should_be_add_basket()
