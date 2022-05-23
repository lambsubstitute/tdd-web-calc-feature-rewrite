import pytest
from app.calculator import Calculator


@pytest.fixture
def calculator():
    calculator = Calculator()
    return calculator


def test_calculator_should_zero_on_initialise(calculator):
    """
    Given I turn on my calculator
    Then it should initialise to 0
    """
    assert calculator.value is 0


def test_calculator_should_concatinate_2_numbers(calculator):
    """
    Given I have an initialised calculator
    When I enter 2 numbers
    Then I want these numbers to be concatinated
    """
    calculation = [1, 2, "="]
    calculator.parse(calculation)
    assert calculator.calculation == [12, "="]


def test_calculator_should_concatinate_3_numbers(calculator):
    """
    Given I have an initialised calculator
    When I enter 3 numbers
    Then I want these numbers to be concatinated
    """
    calculation = [1, 2, 3, "="]
    calculator.parse(calculation)
    assert calculator.calculation == [123, "="]


def test_calculator_should_concatinate_numbers_without_leading_zeros(calculator):
    """
    Given I have an initialised calculator
    When I enter 3 numbers
    Then I want these numbers to be concatinated
    """
    calculation = [0, 0, 0, 0, 1, 2, 3, "="]
    calculator.parse(calculation)
    assert calculator.calculation == [123, "="]


def test_calculator_should_add_2_numbers_together(calculator):
    """
    Given I have an intialised calculator
    When I enter 2 numbers with a plus between them
    Then I want these number to be added
    """
    calculation = [1, "+", 2, "="]
    calculator.parse(calculation)
    assert calculator.value is 3
