from Page.page import Actions
from selenium import webdriver


def test_yandex_search(browser):
    main_page = Actions(browser)
    main_page.enter_site()
    main_page.login()
    main_page.send_mail()
    return "Passed"


el = webdriver.Chrome()
print(test_yandex_search(el))
