class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_start_page(self):
        wd = self.app.wd
        self.app.open_home_page()

    def open_admin_page(self):
        wd = self.app.wd
        wd.get("http://localhost/litecart/admin/")

    def admin_login(self):
        wd = self.app.wd
        self.open_admin_page()
        if len(wd.find_elements_by_name("username")) > 0:
            wd.find_element_by_name("username").click()
            wd.find_element_by_name("username").clear()
            wd.find_element_by_name("username").send_keys("admin")
            wd.find_element_by_name("password").clear()
            wd.find_element_by_name("password").send_keys("admin")
            wd.find_element_by_xpath("//button[@name='login']").click()

