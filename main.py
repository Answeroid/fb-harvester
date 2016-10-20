from selenium import webdriver
from fb_auth import auth
from logger import Logger


def main():
    # TODO add possibility to login to different FB accounts (use csv file to store them)
    # TODO handle all exceptions especially when account was blocked
    # TODO save automatic screenshots from time to time
    # TODO add native system logger from previous log parser project

    log = Logger()
    log.instance()

    log.debug("asdadsasd")

    driver = webdriver.PhantomJS("/home/vkhalin/node_modules/phantomjs-prebuilt/bin/phantomjs")
    driver.get('https://www.facebook.com/')

    auth(driver, log)

    a = 1

if __name__ == '__main__':
    main()
