from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://mail.ru"

    def wait(self, elem, text=None):
        expecting = WebDriverWait(self.driver, 10)
        if text:
            expecting.until(EC.text_to_be_present_in_element((By.XPATH, elem), text))
        else:
            expecting.until(EC.presence_of_element_located((By.XPATH, elem)))

    def enter_site(self):
        e = self.driver.get(self.base_url)
        return e

# driver = webdriver.Chrome()
# driver.get("http://mail.ru")
# assert "Mail.ru" in driver.title
# mail_name = driver.find_element_by_name("login")
# type_password_button = driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[1]')
#
# mail_name.send_keys(Elements.MAIL)
# type_password_button.click()
# wait('//*[@id="mailbox"]/form[1]/button[2]', "Войти")
# import time
# # try:
# #     element = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="mailbox"]/form[1]/button[2]'), "Войти"))
# #
# # finally:
# #     driver.quit()
# to_find_pass_input = driver.find_element_by_name("password")
#
# log_in_button = driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[2]') # find a button to log in
# to_find_pass_input.send_keys(Elements.PASSCODE)
# log_in_button.click()
# wait('//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div[1]/div[1]/div/div/div/div[1]/div/div/a')
# # wait('//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div[1]/div[1]/div/div/div/div[1]/div/div/a/span')
# # try:
# #     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div[1]/div[1]/div/div/div/div[1]/div/div/a/span')))
# # finally:
# #     driver.quit()
#
# button_to_write = driver.find_element_by_xpath('//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div[1]/div[1]/div/div/div/div[1]/div/div/a')
# button_to_write.click()
# wait('/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input')
# # try:
# #     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input')))
# # finally:
# #     driver.quit()
#
# el0 = driver.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input')
# el0.send_keys("arkhipova-1997@yandex.ru")
# el1 = driver.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]')
# el1.send_keys("Hello!")
# el2 = driver.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[2]/div[1]/span[1]/span/span')
# el2.click()
#
