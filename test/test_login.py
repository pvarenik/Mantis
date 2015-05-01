# -*- coding: utf-8 -*-
__author__ = 'pvarenik'


def test_login(app):
    #app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")