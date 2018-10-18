__metaclass__ = type

from normal.Person import Person


class Teacher(Person):
    def __init__(self, name, surname, age, subject):
        super(Teacher, self).__init__(name, surname, age)
        self._subject = subject

    @property
    def subject(self):
        return self._subject
