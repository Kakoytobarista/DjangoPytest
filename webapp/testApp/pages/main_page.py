from .base_page import BasePage
from .locators import MainPageLocators
from .locators import NewsLocators
from selenium.webdriver.common.by import By
from selenium import webdriver


class MainPage(BasePage):
    def should_be_main_url(self):
        str_url = self.url
        print(str_url)
        assert "http://127.0.0.1/" in str_url, "main page do not find in URL"

    def should_see_news_page(self):
        caption = self.browser.find_element(*NewsLocators.CAPTIONS_NEWS).get_attribute('textContent')
        print(caption)
        assert "Новости на сайте" in caption, 'should be "Новости на сайте"'
