# firstly, write test case

from curses.ascii import isdigit as imp
import find_string
import pytest

# 1st test case
def test_ispresent():
    assert find_string.ispresent('Al')

# this test should pass, because name Al is in the list. 

# 2nd test case
def test_nodigit():
    assert find_string.nodigit('N7')

# this test will not pass because N7 is not in the list
