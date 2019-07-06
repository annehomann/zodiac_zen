"""
Program: Zodiac Zen
Author: Anne Homann
Contact: css011906@coderacademy.edu.au
Date: 2019/06/29
Licence: GPLv3
Version: 0.1
Unit testing for Zodiac Zen using Pytest
"""
import requests
from zodiac_zen import greeting
from zodiac_zen import web_scrape

def test_greeting(monkeypatch):

    """ monkeypatch the "input" function, so that it returns "Anne".
    This simulates the user entering "Anne" in the terminal: """

    monkeypatch.setattr('builtins.input', lambda x: "Anne")
    # go about using input() like you normally would:
    first = input("What is your first name?")
    assert first == "Anne"


def test_web_scrape():

    """ GET request to an incorrect URL and
    return a 404. Display that an error would
    occur as the sit cannot be reached """

    url = 'http://annehomamm.github.io/astrology.html'
    resp = requests.get(url)
    assert resp.status_code == 404
