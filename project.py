x = [1, 2, 3]

for element in x:
    print(element)

class Person(object):
    def __init__(self, name:str, gender: str, age: int, height: float) -> float:
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height

        self.happiness: int = 0

    def make_happy(self) -> None:
        self.happiness += 1

    def make_sad(self) -> None:
        self.happiness -= 1