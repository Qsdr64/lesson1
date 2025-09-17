from typing import Literal
import pytest 
from string_utils import  StringUtils

stringtest = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
   ("skypro", "Skypro")
])
def test_capitalize_positive(input_str, expected):
    stringtest = StringUtils()
    assert stringtest.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc")   
])
def test_capitalize_negative(input_str, expected):
    stringtest = StringUtils()
    assert stringtest.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("delprob, expected", [
    (" Skypro", "Skypro")
])
def test_trim_positive(delprob, expected):
    stringtest = StringUtils()
    assert stringtest.trim(delprob) == expected

@pytest.mark.negative
@pytest.mark.parametrize("delprob, expected", [
    ("Skypro", "Skypro")
])
def test_trim_negative(delprob, expected):
    stringtest = StringUtils()
    assert stringtest.trim(delprob) == expected

@pytest.mark.positive
def test_contains_positive():
    stringtest = StringUtils()
    assert stringtest.contains("SkyPro", "S") is True

@pytest.mark.negative
def test_contains_symbol_absent():
    stringtest = StringUtils()
    assert stringtest.contains("SkyPro", "U") is False

@pytest.mark.positive
def test_delete_symbol_present():
    stringtest = StringUtils()
    result = stringtest.delete_symbol("SkyPro", "k")
    assert result == "SyPro"

@pytest.mark.negative
def test_delete_symbol_absent():
    stringtest = StringUtils() 
    result = stringtest.delete_symbol("SkyPro", "X")
    assert result == "SkyPro"