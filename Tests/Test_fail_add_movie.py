from conftest import app
from model.User import User

def test_add_new_movie(app):
    app.login(User.Admin())
    assert app.is_logged_in()
    app.fail_add_new_movie()



