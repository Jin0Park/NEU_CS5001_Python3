"""
Jin Young Park
CS5001 Fall 2021
HW05 test_recipe.py
Test remove_whitespaces and name_validate functions from recipe.py
"""
from recipe import remove_whitespaces, name_validate


def test_remove_whitespaces():
    assert(remove_whitespaces(["   a    ", " ab", " ba"]) == ["a", "ab", "ba"])
    assert(remove_whitespaces(["  AB", "  CD ", "EF  "]) == ["AB", "CD", "EF"])


def test_name_validate():
    assert(name_validate("Egg and Soldier") == "egg_and_soldier")
    assert(name_validate("BB&Q") == "bbq")
    assert(name_validate("honey DEW !!!!") == "honey_dew")
    assert(name_validate("PB on toast") == "pb_on_toast")
