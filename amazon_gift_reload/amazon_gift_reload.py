"""Main module."""
# https://pypi.org/project/chromedriver-py/
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class AmazonGiftReloader(object):
    RELOAD_URL = "https://www.amazon.com/gp/product/B086KKT3RX"
    SIGNIN_URL = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fproduct%2FB086KKT3RX%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
    PLACE_ORDER_XPATH = "/html/body/div[5]/div/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input"

    PAGE_LOAD_WAIT_SECS = 10

    def __init__(self, reload_value, number_of_reloads, email, password) -> None:
        self.logger = logging.getLogger("amazon_gift_reloader.AmazonGiftReloader")

        self.reload_value = reload_value
        self.number_of_reloads = number_of_reloads
        self.email = email
        self.password = password

        self.driver = webdriver.Chrome()

    def run(self):
        self.sign_in()

        reload_total = self.number_of_reloads * self.reload_value

        for i in range(1, self.number_of_reloads + 1):
            print(
                f"[{i}/{self.number_of_reloads}][${i * self.reload_value}/${reload_total}] processing reload ..."
            )
            if self.RELOAD_URL not in self.driver.current_url:
                self.driver.get(self.RELOAD_URL)
            self.input_reload_value()
            self.submit_order()
            print(
                f"[{i}/{self.number_of_reloads}][${i * self.reload_value}/${reload_total}] reload successful!"
            )
        return

    def sign_in(self):
        self.logger.info(f"logging in as {self.email}")
        self.driver.get(self.SIGNIN_URL)

        email_field = self.find_elem_by_id("ap_email")
        self.input_value(email_field, self.email)

        pass_field = self.find_elem_by_id("ap_password")
        self.input_value(pass_field, self.password)

        assert self.find_elem_by_id("nav-item-signout")
        return

    def find_elem_by_id(self, id):
        self.logger.info(f"finding element with id {id}")
        elem = WebDriverWait(self.driver, self.PAGE_LOAD_WAIT_SECS).until(
            EC.presence_of_element_located((By.ID, id))
        )
        return elem

    def input_value(self, field, value):
        self.logger.info(f"sending value to field {field.get_attribute('id')}")
        field.clear()
        field.send_keys(value)
        field.send_keys(Keys.RETURN)
        return

    def input_reload_value(self):
        amount_field = self.find_elem_by_id("gcui-asv-reload-form-custom-amount")
        self.input_value(amount_field, self.reload_value)
        assert self.find_elem_by_id("placeYourOrder")
        return

    def submit_order(self):
        self.logger.info("submitting the order!")
        WebDriverWait(self.driver, self.PAGE_LOAD_WAIT_SECS).until(
            EC.element_to_be_clickable((By.XPATH, self.PLACE_ORDER_XPATH))
        ).click()
        return
