# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from conftest import app
from model.User import *

def test_login(app):
    app.go_to_home_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()

def test_fail_login(app):
    app.go_to_home_page()
    app.login(User.Fail_user())
    assert app.is_not_logged_in()

