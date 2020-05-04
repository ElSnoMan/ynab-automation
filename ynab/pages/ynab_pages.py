from pylenium import Pylenium

from ynab.pages.budget import BudgetPage
from ynab.pages.login import LoginPage


class Pages:
    def __init__(self, py: Pylenium):
        self.py = py
        self.login = LoginPage(py)
        self.budget = BudgetPage(py)
