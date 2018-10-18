class Person:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age

    def get_full_name(self):
        return self._surname + " " + self._name[:1]

