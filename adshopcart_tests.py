import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators

class AdvantageShoppingAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_adshopcart():
        methods.setUp()
        methods.create_new_user()
        methods.check_new_user_account()
        methods.login_with_new_credential()
        methods.check_text()
        methods.check_top_nav_menu()
        methods.check_contact_us_form()
        methods.delete_user()
        methods.login_with_deleted_user()
        methods.tearDown()


