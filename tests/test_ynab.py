from tests import constants
import pytest

from ynab.pages.ynab_pages import Pages


@pytest.fixture
def login(py):
    py.visit('https://app.youneedabudget.com/')
    py.get('#request_data_email').type('david.herrera83@gmail.com')
    py.get('#request_data_password').type(constants.YNAB_PASSWORD)
    py.get('#login').click()


@pytest.fixture
def login_pom(py, ynab):
    return ynab.login\
        .visit()\
        .login_to('david.herrera83@gmail.com', constants.YNAB_PASSWORD)


@pytest.fixture
def ynab(py):
    return Pages(py)


def test_can_login_to_ynab(login_pom, ynab):
    assert ynab.py.contains('Herrera Family')


def test_i_have_money_to_budget(login_pom, ynab):
    assert '-' not in ynab.budget.get_budget()
