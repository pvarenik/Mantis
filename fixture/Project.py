__author__ = 'pvarenik'
import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add(self, project):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.19/manage_proj_page.php")
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_css_selector('input[value="Add Project"]').click()

    def exist(self, project):
        wd = self.app.wd
        time.sleep(10)
        existance = wd.find_elements_by_xpath("//a[text()='{0}']".format(project.name))
        return len(existance) > 0

    def get_list(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.19/manage_proj_page.php")
        list = wd.find_elements_by_css_selector('tr[class="row-1"]') + wd.find_elements_by_css_selector('tr[class="row-2"]')
        return list[:-1]

    def delete_first(self, list):
        wd = self.app.wd
        wd.find_elements_by_xpath("//a[text()='{0}']".format(list[0].text.split(" ")[0]))[0].click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()

