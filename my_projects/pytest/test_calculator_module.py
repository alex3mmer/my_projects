import pytest
import calculator_module

class TestCalculator:
    """Tests basic functionality of calculator_module."""

    @pytest.fixture
    def sample_number(self) -> int:
        return 10
    
    def test_increment(self, sample_number) -> None:
        assert calculator_module.increment_by_one(sample_number) == 11

    def test_decrement(self, sample_number) -> None:
        assert calculator_module.decrement_by_one(sample_number) == 9

class TestCalculatorTypeValidation:
    """Tests type validation in calculator_module."""

    @pytest.mark.parametrize("input", 
        [
        "5",
        None,
        False,
        ]
    )
    @pytest.mark.parametrize("operation", 
        [
        calculator_module.increment_by_one, 
        calculator_module.decrement_by_one
        ]
    )
    def test_calculator_module_type_error(self, input, operation) -> None:
        with pytest.raises(TypeError):
            operation(input)
