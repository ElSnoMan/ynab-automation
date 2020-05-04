from pylenium import Pylenium


class BudgetPage:
    def __init__(self, py: Pylenium):
        self.py = py

    def get_budget(self) -> str:
        return self.py.get('[class="budget-header-totals-amount-value"]')\
            .get_attribute('title')
