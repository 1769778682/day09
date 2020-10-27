import time
from selenium.webdriver.support.select import Select

from admin_goods.utils import Driver


class BaseAdd(object):
    def __init__(self):
        self.driver = Driver().get_driver()

    def find_elem(self, element):
        return self.driver.find_element(*element)


class BaseAction(object):
    def input_text(self, elem, text):
        elem.send_keys(text)

    def select(self, elem, text):
        time.sleep(2)
        Select(elem).select_by_visible_text(text)
