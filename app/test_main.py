from app.main import get_human_age
import pytest


def test_should_raise_type_error():
    with pytest.raises(TypeError):
        get_human_age("ten", "twenty")


def test_should_return_list():
    cat_years = 10
    dog_years = 10
    result = get_human_age(cat_years, dog_years)
    assert isinstance(result, list)
    
