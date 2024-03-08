"""Demonstrate code coverage and path coverage."""
#tests\test_coverage.py
# Standard Library

# 3rd Library
import pytest

# Project Library
from experiment.myproj import max, total
# tests/test_leap_year.py
# tests/test_leap_year.py
import pytest
from experiment.myproj import is_leap_year

@pytest.mark.parametrize("year, expected", [
    (1600, True),  
    (1700, False), 
    (1800, False), 
    (1900, False), 
    (1996, True),  
    (2000, True),  
    (2004, True),  
    (2100, False), 
    (2200, False), 
    (2300, False), 
    (2400, True),  
    (2500, False), 
    (2021, False), 
    (2024, True),  
    (2028, True),  
])
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected

