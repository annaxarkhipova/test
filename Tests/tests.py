from Page.page import Actions

def test_yandex_search(browser):
    main_page = Actions(browser)
    main_page.enter_site()
    main_page.login()
    main_page.send_mail()
    # elements = main_page.check_navigation_bar()
    # assert "Картинки" and "Видео" in elements