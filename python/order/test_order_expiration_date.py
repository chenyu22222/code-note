import pytest
from order_expiration_date import get_expiration_date


def test_normal_date():
    assert get_expiration_date(2016, 11, 10) == [2016, 12, 10]


def test_over_year_date():
    assert get_expiration_date(2016, 12, 10) == [2017, 1, 10]


def test_expired_in_feb_date():
    assert get_expiration_date(2017, 1, 30) == [2017, 2, 28]


if __name__ == '__main__':
    pytest.main()