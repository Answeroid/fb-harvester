from selenium import webdriver


def main():
    # TODO add possibility to login to different FB accounts (use csv file to store them)
    # TODO handle all exceptions especially when account was blocked
    # TODO add possibility to grab users to find from data/*.csv


    driver = webdriver.PhantomJS("/home/vkhalin/node_modules/phantomjs-prebuilt/bin/phantomjs")
    driver.get('https://www.facebook.com/')
    b = driver.find_elements_by_class_name("inputtext")
    c = driver.find_elements_by_css_selector("#email")
    email = c[0]
    email.click()
    email.send_keys("AZAZAZAZAZAAZAZ")
    z = 1


if __name__ == '__main__':
    main()
