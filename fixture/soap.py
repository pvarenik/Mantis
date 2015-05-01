__author__ = 'pvarenik'
from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, user, password):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(user, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, user, password):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            return client.service.mc_projects_get_user_accessible(user, password)
        except WebFault:
            return None