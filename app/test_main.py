from app.main import get_human_age
import pytest
    

def test_should_return_list_of_integers():
    result = get_human_age(10, 10)
    assert len(result) == 2


def test_should_return_zero_when_both_arg_are_zero():
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_should_return_zero_when_age_less_fifteen():
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_age_fifteen():
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_two_year_when_age_twentyfour():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_when_age_twentyseven():
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_three_cats_and_two_dogs():
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_three_when_age_more_twentynine():
    assert get_human_age(29, 29) == [3, 3]
