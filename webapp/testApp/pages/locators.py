from selenium.webdriver.common.by import By


class MainPageLocators(object):
    MAIN_PAGE_BUTTON = (By.CSS_SELECTOR, "body > aside > ul > a:nth-child(1)")
    NEWS_PAGE_BUTTON = (By.CSS_SELECTOR, "body > aside > ul > a:nth-child(3)")


class NewsLocators:
    CAPTIONS_NEWS = (By.XPATH, "/html/body/main/div")
