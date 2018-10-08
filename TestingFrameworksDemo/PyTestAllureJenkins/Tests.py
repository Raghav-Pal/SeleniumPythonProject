from selenium.webdriver.common.by import By

page = "page"
username_el = "username"
password_el = "password"
submit = "//input[@type='submit']"
expected_url = "my/"


def open_url(driver, url):
   driver.get(url)
   driver.find_element(By.ID, page)


def add_field(driver, value, field):
   username_field = driver.find_element(By.NAME, field)
   username_field.clear()
   username_field.send_keys(value)


def add_credentials(driver, username, password):
   add_field(driver, username, username_el)
   add_field(driver, password, password_el)


def submit_form(driver):
   driver.find_element(By.XPATH, submit).click()


def verify_url(driver, url):
   assert (url + expected_url) == driver.current_url