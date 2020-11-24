import pytest
from kompetenzen.views import *

# testing the percent function
def test_percent():
    result = percent(1,100)
    assert result == 1
    result = percent(0, 0)
    assert result == 0
    result = percent(4,20)
    assert result == 20
    result = percent("abc","def")
    assert result == 0