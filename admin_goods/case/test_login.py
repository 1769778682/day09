import logging
import time
import pytest
from page.page_admin import Work
from utils import Driver


@pytest.mark.run(order=1)
class TestShop:

    def setup_class(self):
        self.driver = Driver().get_driver()
        self.login = Work()

    def setup(self):
        time.sleep(2)
        self.driver.get("http://localhost/Admin/Admin/login")

    # @staticmethod
    # def teardown_class():
    #     Driver().quit_web()

    @pytest.mark.parametrize(("username", "password", "verify"), [("admin", "123456", "8888")])
    def test_login(self, username, password, verify):
        logging.info("start->proxy--->{}{}{}".format(username, password, verify))
        self.login.admin_login(username, password, verify)
