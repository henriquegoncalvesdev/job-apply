class ApplicationHandler:
    def __init__(self, driver, form_filler):
        self.driver = driver
        self.form_filler = form_filler

    def apply_to_job(self, job_url, form_data):
        self.driver.get(job_url)
        # TODO: Wait for page load and detect application form
        # Use form_filler to fill and submit
        self.form_filler.fill_form(form_data)
        # TODO: Confirm application status
        return True
