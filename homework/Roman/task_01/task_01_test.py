import pytest

from task_01 import convert_n_to_m


def test_1():
    assert '102' == convert_n_to_m("0123", 5, 6)


def test_2():
    assert 'False' == convert_n_to_m("123", 3, 5)


def test_3():
    assert 'False' == convert_n_to_m(-123.0, 11, 16)


def test_4():
    assert '32E7' == convert_n_to_m('A1Z', 36, 16)


def test_5():
    assert '300' == convert_n_to_m('123', 4, 3)

