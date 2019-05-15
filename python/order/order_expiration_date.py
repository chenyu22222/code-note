#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long


ORDER_MONTHS = 1


def get_expiration_date(year: int, month: int, day: int) -> list:
    """
    1. 根据年份判断闰年
    2. 根据闰年判断二月天数 并设置成一个月份字典
    3. 加月份并通过月份字典判断是否合法 不合法则根据月份字典进行调整
    4. 遇到需要加年份的进行年份的增加 利用月份字典判断日期是否合法
    :param year:
    :param month:
    :param day:
    :return:
    """
    month_dict = dict()
    big = tuple(range(1, 32))
    small = tuple(range(1, 31))

    month_dict.update({month: big for month in [1, 3, 5, 7, 8, 10, 12]})
    month_dict.update({month: small for month in [4, 6, 9, 11]})

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # leap year
        month_dict[2] = tuple(range(1, 30))
    else:
        # not leap year
        month_dict[2] = tuple(range(1, 29))

    if month + ORDER_MONTHS > 12:
        # over the year
        _year = year + (month + ORDER_MONTHS) // 12
        _month = (month + ORDER_MONTHS) % 12
    else:
        _year = year
        _month = month + ORDER_MONTHS

    if day > month_dict[_month][-1]:
        _day = month_dict[_month][-1]
    else:
        _day = day

    return [_year, _month, _day]