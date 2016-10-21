import csv


def auth(driver, logger):
    """
    Tries to authorize to FB with given credentials from file
    :param logger: logger instance
    :param driver: webdriver instance
    :return:
    """
    # TODO add possibility to grab users to find from data/*.csv
    try:
        logger.debug("Reading fb credentials file...")
        with open("data/creds.csv", "rb") as file_:
            creds = csv.reader(file_, delimiter=',')
            for cred in creds:
                login = cred[0]
                passw = cred[1]
            logger.debug("Reading completed...")
    except Exception as e:
        logger.debug(e)

    try:
        logger.debug("Pasting login password to fb page and trying to login...")
        email = driver.find_element_by_css_selector("#email")
        email.send_keys(str(login))

        password = driver.find_element_by_css_selector("#pass")
        password.send_keys(str(passw))

        submit = driver.find_element_by_css_selector("#loginbutton")
        submit.click()
        logger.debug("Login done...")
    except Exception as e:
        print logger.debug(e)
