from normal.Person import Person

__metaclass__ = type


class Student(Person):
    """Класс описывает конкретного ученика школы"""

    def __init__(self, name, surname, age, f_name, f_surname, m_name, m_surname):
        super(Student, self).__init__(name, surname, age)
        self._f_name = f_name
        self._f_surname = f_surname
        self._m_name = m_name
        self._m_surname = m_surname

    @property
    def surname_student(self):
        return self._surname

    @property
    def name_student(self):
        return self._name

    @property
    def mother(self):
        return self._m_surname + " " + self._m_name

    @property
    def father(self):
        return self._f_surname + " " + self._f_name

    '''@property
    def dad_fio(self):
        return self._dad_fio'''
