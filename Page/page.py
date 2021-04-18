from Base.base import BasePage
from selenium.webdriver.common.by import By


class Elements:
    passcode = "I-3iRcUAuia7"
    mail = "annaarkhx@mail.ru"
    type_password = '//*[@id="mailbox"]/form[1]/button[1]'
    button_to_login = '//*[@id="mailbox"]/form[1]/button[2]'
    new_mail_icon = '//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div[1]/div[1]/div/div/div/div[1]/div/div/a'
    input_TO = '/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input'
    body_field = '/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]'
    button_to_send = '/html/body/div[15]/div[2]/div/div[2]/div[1]/span[1]/span/span'


class Actions(BasePage):
    def login(self):
        self.enter_site()
        mail_name = self.driver.find_element_by_name("login")
        type_password_button = self.driver.find_element_by_xpath(Elements.type_password)
        mail_name.send_keys(Elements.mail)
        type_password_button.click()
        self.wait(Elements.button_to_login, "Войти")
        to_find_pass_input = self.driver.find_element_by_name("password")

        log_in_button = self.driver.find_element_by_xpath(Elements.button_to_login)
        to_find_pass_input.send_keys(Elements.passcode)
        log_in_button.click()
        self.wait(Elements.new_mail_icon)

    def send_mail(self, recipient="arkhipova-1997@yandex.ru", message="Hello!"):
        button_to_write = self.driver.find_element_by_xpath(Elements.new_mail_icon)
        button_to_write.click()
        self.wait(Elements.input_TO)
        recipient_mail_field = self.driver.find_element_by_xpath(Elements.input_TO)
        recipient_mail_field.send_keys(recipient)
        body = self.driver.find_element_by_xpath(Elements.body_field)
        body.send_keys(message)
        el2 = self.driver.find_element_by_xpath(Elements.button_to_send)
        el2.click()

