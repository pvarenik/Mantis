__author__ = 'pvarenik'
from model.project import Project
import random
import string


def random_str(prefix="test_", maxlen=10):
    sym = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(sym) for i in range(maxlen)])

def test_delete_project(app):
    username = app.config["webadmin"]["username"]
    password = app.config["webadmin"]["password"]
    projects_list_old = app.soap.get_projects_list(username, password)
    if len(projects_list_old) == 0:
        name = random_str()
        app.project.add(Project(name=name))
        projects_list_old = app.soap.get_projects_list(username, password)
    app.project.delete_first(app.project.get_list())
    projects_list_new = app.soap.get_projects_list(username, password)
    assert (len(projects_list_old) - len(projects_list_new)) == 1