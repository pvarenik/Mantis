__author__ = 'pvarenik'
import re

class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get(self.app.base_url + "/signup_page.php")
        # Enter username
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        # Enter email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        # Signup button
        wd.find_element_by_css_selector('input[value="Signup"]').click()
        # Get url from mail
        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_url(mail)
        # Confirm
        wd.get(url)
        # Enter password
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        # Confirm password
        wd.find_element_by_name("password_confirm").click()
        wd.find_element_by_name("password_confirm").clear()
        wd.find_element_by_name("password_confirm").send_keys(password)
        # Confirm button
        wd.find_element_by_css_selector('input[value="Update User"]').click()

    def extract_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)