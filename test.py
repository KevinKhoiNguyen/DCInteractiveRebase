import pytest  

from project import Person

@pytest.fixture
def test_person() -> Person:
    return Person(name="Mike", gender="Male", age=23, height=180)

def test_person_make_happy(test_person) -> None:
    test_person.make_happy()
    assert test_person.happiness == 1
