import pytest
import calculator_module

def test_my_calculator_module() -> None:
    """Tests all functions in my_calculator_module."""
    assert calculator_module.increment_by_one(3) == 4

    assert calculator_module.decrement_by_one(3) == 2

@pytest.mark.parametrize("a", 
    [
    ("5"),
    (None),
    (False),
    ]
)
def test_my_calculator_module_type_error(a) -> None:
    with pytest.raises(TypeError):
        calculator_module.increment_by_one(a)
        calculator_module.decrement_by_one(a)
