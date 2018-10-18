from normal.Student import Student


class Study_class:
    def __init__(self, name, **args):
        self._study_class = {"number": name.split()[0], "letter": name.split()[1]}
        self._students = args.get("students")
        self._teachers = args.get("teachers")

    def get_number_class(self):
        return self._study_class["number"]

    def get_class(self):
        return self._study_class.get("number") + " " + self._study_class.get("letter")

    def get_students_fullname(self):
        return [student.get_full_name() for student in self._students]

    def get_students_objects(self):
        return [student for student in self._students]

    def get_teachers(self):
        return [teacher.get_full_name() for teacher in self._teachers]

    def get_object_teachers(self):
        return [teacher for teacher in self._teachers]
