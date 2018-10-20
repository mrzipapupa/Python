from normal.Person import Person
from normal.Student import Student
from normal.Teacher import Teacher

class School:
    """Класс описывает школу как совокупность учителей и классов"""

    def __init__(self, name, *classes):
        self.name = name
        self._classes = classes

    def get_classes(self):
        return [class_r.get_class() for class_r in self._classes]

    def get_object_classes(self):
        return [class_r for class_r in self._classes]

