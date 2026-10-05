import pytest
import main

def test_main() -> None:
    """Tests all functions in main."""
    assert main.increment_by_one(3) == 4

@pytest.mark.parametrize("a", 
    [
    ("5"),
    (None),
    ]
)
def test_main_type_error(a) -> None:
    with pytest.raises(TypeError):
        main.increment_by_one(a)