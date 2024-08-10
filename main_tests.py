import pytest
from main import Calculator


@pytest.mark.parametrize(
    ('initial', 'input_n', 'expected'),
    (
        (5, 5, 10),
        (-3, -5, -8),
        (0, 0, 0)
    )
)
def test_arithmetic_add(initial, input_n, expected):
    calc = Calculator()
    assert calc.add(initial + input_n) == expected

def test_arithmetic_sub(calculator: Calculator):
    assert Calculator.substract(-3)==-3
