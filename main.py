from selenium import webdriver


def main():
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
