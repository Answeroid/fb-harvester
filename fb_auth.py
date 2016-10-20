def auth(driver, logger):
    """
    Tries to authorize to FB with given credentials from file
    :param logger: logger instance
    :param driver: webdriver instance
    :return:
    """
    # TODO add possibility to grab users to find from data/*.csv
    try:
        with open("data/creds.csv", "r") as file_:
            pass
    except Exception as e:
        logger.debug(e)

    login = "login"
    passw = "password"

    try:
        email = driver.find_element_by_css_selector("#email")
        email.send_keys(str(login))

        password = driver.find_element_by_css_selector("#pass")
        password.send_keys(str(passw))

        submit = driver.find_element_by_css_selector("#loginasd")
        submit.click()
    except Exception as e:
        print logger.debug(e)
