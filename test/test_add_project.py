__author__ = 'pvarenik'
from model.project import Project
import random
import string


def random_str(prefix="test_", maxlen=10):
    sym = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(sym) for i in range(maxlen)])

def test_add_project(app):
    name = random_str()
    app.project.add(Project(name=name))
    assert app.project.exist(Project(name=name))