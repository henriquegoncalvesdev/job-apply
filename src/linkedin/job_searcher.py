from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class JobSearcher:
    def __init__(self, driver):
        self.driver = driver

    def go_to_jobs_page(self):
        self.driver.get('https://www.linkedin.com/jobs/')
        time.sleep(2)

    def search_jobs(self, keywords, location):
        self.go_to_jobs_page()
        search_box = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search jobs"]')
        location_box = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search location"]')
        search_box.clear()
        search_box.send_keys(keywords)
        location_box.clear()
        location_box.send_keys(location)
        location_box.send_keys(Keys.RETURN)
        time.sleep(3)
        # TODO: Extract job listings
        return []
