from utils import Driver


class BaseAdmin:
    def __init__(self):
        self.driver = Driver.get_driver()

    def base_admin(self, element):
        return self.driver.find_element(*element)


class BaseAction:

    def base_action(self, elem, text):
        elem.clear()
        elem.send_keys(text)