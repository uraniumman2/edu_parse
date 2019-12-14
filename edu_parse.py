from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math


class EduParse:
    def __init__(self, iin_text, password_text, webdriver_path):
        self.iin_text = iin_text
        self.password_text = password_text
        self.webdriver_path = webdriver_path

    def parse(self):
        convert = lambda x: float(x) * 0.3
        calculate = lambda r: math.ceil((89.5 - r) / 0.4)
        browser = webdriver.Chrome(executable_path=self.webdriver_path)
        browser.maximize_window()
        browser.get("https://edu.enu.kz/")
        time.sleep(3)
        # AUTHORIZATION
        iin = browser.find_element_by_name("iin")
        iin.clear()
        iin.send_keys(self.iin_text)
        password = browser.find_element_by_name("password")
        password.clear()
        password.send_keys(self.password_text)
        submit = browser.find_element_by_name("Submit1")
        submit.send_keys(Keys.RETURN)
        time.sleep(3)

        #GETTING DATA
        browser.get("https://edu.enu.kz/current_progress_gradebook_student")
        tbody = browser.find_element_by_tag_name("tbody")
        trs = tbody.find_elements_by_tag_name("tr")
        for tr in trs:
            tds = tr.find_elements_by_tag_name("td")
            if len(tds) == 29:
                try:
                    print(tds[2].text + "\n" + tds[0].text + ":" + str(
                        calculate(convert(tds[11].text) + convert(tds[21].text))))
                except ValueError:
                    pass
        browser.close()
