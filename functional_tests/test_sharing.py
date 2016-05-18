from selenium import webdriver
from .base import FunctionalTest

from .management.commands.create_session import create_pre_authenticated_session

def quit_if_possible(browser):
    try:
        browser.quit()
    except:
        pass

class SharingTest(FunctionalTest):

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is logged-in user
        create_pre_authenticated_session('edith@example.com')