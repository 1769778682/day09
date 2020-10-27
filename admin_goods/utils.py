import time

from selenium import webdriver


class Driver:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(30)
        return cls.__driver

    @classmethod
    def quit_web(cls):
        if cls.__driver is not None:
            time.sleep(3)
            cls.__driver.quit()
            cls.__driver = None


if __name__ == '__main__':
    Driver().get_driver()
    Driver().quit_web()
