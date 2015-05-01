__author__ = 'pvarenik'
from model.project import Project
import random
import string


def random_str(prefix="test_", maxlen=10):
    sym = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(sym) for i in range(maxlen)])

def test_add_project(app):
    projects_list_old = app.project.get_list()
    if len(projects_list_old) == 0:
        name = random_str()
        app.project.add(Project(name=name))
        projects_list_old = app.project.get_list()
    app.project.delete_first(projects_list_old)
    projects_list_new = app.project.get_list()
    assert (len(projects_list_old) - len(projects_list_new)) == 1