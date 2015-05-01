__author__ = 'pvarenik'
import random
import string


def random_str(prefix="test_", maxlen=10):
    sym = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(sym) for i in range(maxlen)])

def test_sign_up_new_account(app):
    username = random_str("user_")
    email = username + "@localhost"
    password = "test"
    app.james.ensure_user_exist(username, password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)

