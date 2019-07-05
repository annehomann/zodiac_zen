from main import greeting
from main import get_readings

def test_greeting(monkeypatch):

    # monkeypatch the "input" function, so that it returns "Anne".
    # This simulates the user entering "Anne" in the terminal:
    monkeypatch.setattr('builtins.input', lambda x: "Anne")

    # go about using input() like you normally would:
    first = input("What is your first name?")
    assert first == "Anne"