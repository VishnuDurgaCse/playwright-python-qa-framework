import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate_to_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    assert inventory.is_inventory_page(), "Login failed — inventory page not visible"

def test_invalid_login(page):
    login = LoginPage(page)
    login.navigate_to_login()
    login.login("wrong_user", "wrong_password")
    error = login.get_error_message()
    assert "Username and password do not match" in error

def test_empty_username(page):
    login = LoginPage(page)
    login.navigate_to_login()
    login.login("", "secret_sauce")
    error = login.get_error_message()
    assert "Username is required" in error

def test_empty_password(page):
    login = LoginPage(page)
    login.navigate_to_login()
    login.login("standard_user", "")
    error = login.get_error_message()
    assert "Password is required" in error

def test_logout(page):
    login = LoginPage(page)
    login.navigate_to_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.logout()
    assert page.url == "https://www.saucedemo.com/"