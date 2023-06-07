import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_exampple(setup):
    assert True
    setup.get('https://www.delrayo.tech')
    assert setup.title == "DelRayo.tech - Delrayo Tech"

def test_two():
    assert 1 == 1

