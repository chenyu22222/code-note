import pytest
from order_expiration_date import get_expiration_date


def test_normal_date():
    assert get_expiration_date(2016, 11, 10) == [2016, 12, 10]


def test_over_year_date():
    assert get_expiration_date(2016, 12, 10) == [2017, 1, 10]


def test_expired_in_feb_date():
    assert get_expiration_date(2017, 1, 30) == [2017, 2, 28]


def test_order_3_months_to_feb_date(mocker):
    mocker.patch("order_expiration_date.ORDER_MONTHS", 3)
    assert get_expiration_date(2015, 11, 30) == [2016, 2, 29]


def test_order_3_months_to_feb_date2(mocker):
    mocker.patch("order_expiration_date.ORDER_MONTHS", 3)
    assert get_expiration_date(2016, 11, 29) == [2017, 2, 28]


def test_order_3_months_date(mocker):
    mocker.patch("order_expiration_date.ORDER_MONTHS", 3)
    assert get_expiration_date(2017, 1, 30) == [2017, 4, 30]


def test_order_6_months_date(mocker):
    mocker.patch("order_expiration_date.ORDER_MONTHS", 6)
    assert get_expiration_date(2017, 2, 28) == [2017, 8, 28]


def test_order_12_months_date(mocker):
    mocker.patch("order_expiration_date.ORDER_MONTHS", 12)
    assert get_expiration_date(2017, 1, 1) == [2018, 1, 1]


if __name__ == '__main__':
    pytest.main()