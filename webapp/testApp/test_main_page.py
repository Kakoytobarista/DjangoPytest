import pytest
from pages.main_page import MainPage


main_link = "http://127.0.0.1/"


class TestFromMainPage(object):
    def test_guest_can_go_to_main_page(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.should_be_main_url()

    def test_guest_can_go_to_news(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.go_to_news(browser)
        page.should_see_news_page()
