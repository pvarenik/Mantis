__author__ = 'pvarenik'
from telnetlib import Telnet


class JamesHelper:

    def __init__(self, app):
        self.app = app

    def ensure_user_exist(self, username, password):
        james_config = self.app.config["james"]
        session = JamesHelper.Session(
            james_config["host"], james_config["port"], james_config["username"], james_config["password"])
        if session.is_user_registered(username):
            session.reset_password(username, password)
        else:
            session.create_user(username, password)
        session.quit()


    class Session:

        def __init__(self, host, port, username, password):
            self.telnet = Telnet(host, port, 5)
            self.read_until("Login id:")
            self.write(username)
            self.read_until("Password:")
            self.write(password)
            self.read_until("Welcome root. HELP for a list of commands")

        def read_until(self, text):
            self.telnet.read_until(text.encode("ascii"), 5)

        def write(self, text):
            self.telnet.write((text + "\n").encode("ascii"))

        def is_user_registered(self, username):
            self.write("verify %s" % username)
            res = self.telnet.expect([b"exists", b"does not exist"])
            return res[0] == 0

        def create_user(self, username, password):
            self.write("adduser %s %s" % (username, password))
            self.read_until("User %s added" % username)

        def reset_password(self, username, password):
            self.write("setpassword %s %s" % (username, password))
            self.read_until("Password fo %s reset" % username)

        def quit(self):
            self.write("quit")