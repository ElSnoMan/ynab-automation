from pylenium import Pylenium

from ynab.pages.budget import BudgetPage


class LoginPage:
    def __init__(self, py: Pylenium):
        self.py = py

    # SELECTORS
    EMAIL_FIELD = '#request_data_email'

    # ACTIONS #

    def visit(self) -> 'LoginPage':
        self.py.visit('https://app.youneedabudget.com/')
        return self

    def login_to(self, email, password) -> BudgetPage:
        self.py.get(self.EMAIL_FIELD).type(email)
        self.py.get('#request_data_password').type(password)
        self.py.get('#login').click()
        return BudgetPage(self.py)
