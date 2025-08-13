import time

class Navigator:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.get('https://www.linkedin.com/login')
        time.sleep(2)
        email_input = self.driver.find_element('id', 'username')
        password_input = self.driver.find_element('id', 'password')
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input.submit()
        time.sleep(3)
