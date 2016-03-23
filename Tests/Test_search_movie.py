from conftest import app
from model.User import User

def test_search_All_Movies_In_Databases(app):
    app.login(User.Admin())
    assert app.is_logged_in()
    app.search_movie()

