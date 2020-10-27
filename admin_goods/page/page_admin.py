from selenium.webdriver.common.by import By



# 对象库层
from admin_goods.base.base_admin import BaseAdmin, BaseAction


class GetElem(BaseAdmin):
    def __init__(self):
        super().__init__()
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.verify = (By.NAME, "vertify")
        self.login = (By.NAME, "submit")

    def find_username(self):
        return self.base_admin(self.username)

    def find_password(self):
        return self.base_admin(self.password)

    def find_verify(self):
        return self.base_admin(self.verify)

    def find_login(self):
        return self.base_admin(self.login)


#  操作层
class Action(BaseAction):
    def __init__(self):
        self.driver = GetElem()

    def input_username(self, username):
        self.base_action(self.driver.find_username(), username)

    def input_password(self, password):
        self.base_action(self.driver.find_password(), password)

    def input_verify(self, verify):
        self.base_action(self.driver.find_verify(), verify)

    def click_login(self):
        self.driver.find_login().click()


# 业务层
class Work:
    def __init__(self):
        self.login = Action()

    def admin_login(self, username, password, verify):
        self.login.input_username(username)
        self.login.input_password(password)
        self.login.input_verify(verify)
        self.login.click_login()
