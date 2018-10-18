from normal.Student import Student
from normal.Person import Person
from normal.Teacher import Teacher
from normal.Study_class import Study_class
from normal.School import School


# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

def get_subjects(student, school):
    _student = student.get_full_name()
    for _class in school.get_object_classes():
        for stud in _class.get_students_fullname():
            if stud == _student:
                for teacher in _class.get_object_teachers():
                    print(teacher.subject)
                return


if __name__ == '__main__':
    student1 = Student("Иван", "Иванов", "15", "Петр", "Петров", "Елизавета", "Крымская")
    student2 = Student("Федор", "Федоров", "14", "Илья", "Ильин", "Виктория", "Левая")
    student3 = Student("Артем", "Иванов", "15", "Петр", "Петров", "Елизавета", "Крымская")
    student4 = Student("Дарья", "Пливина", "15", "Виктор", "Приливин", "Анна", "Сеева")
    student5 = Student("Валерия", "Блатова", "14", "Андрей", "Воробьев", "Марина", "Сергеева")
    student6 = Student("Анна", "Болконская", "15", "Максим", "Скоробеев", "Валя", "Лобанова")

    teacher1 = Teacher("Мария", "Васильевна", "31", "Математика")
    teacher2 = Teacher("Евгения", "Левина", "21", "Русский язык")
    teacher3 = Teacher("Алина", "Евлеева", "35", "Математика")

    class1 = Study_class("9 A", students=(student1, student2), teachers=(teacher1, teacher2))
    class2 = Study_class("9 Б", students=(student3,), teachers=(teacher1,))
    class3 = Study_class("8 А", students=(student4, student5), teachers=(teacher2, teacher3))

    school1 = School("1891", class1, class2, class3)

    # 1. Получить полный список всех классов школы
    print("Список классов в школе: ")
    print(school1.get_classes())
    print()
    # 2. Получить список всех учеников в указанном классе
    print("Список учеников класса: ")
    print(class1.get_students_fullname())
    print()
    # 3. Получить список всех предметов указанного ученика
    #  (Ученик --> Класс --> Учителя --> Предметы)
    print("Список предметов ученика: ")
    get_subjects(student3, school1)
    # 4. Узнать ФИО родителей указанного ученика
    print("\nУченик: {0}\nМать: {1}\nОтец: {2}\n".format(student1.get_full_name(), student1.mother, student1.father))
    # 5. Получить список всех Учителей, преподающих в указанном классе
    print("Список учителей класса: ")
    print(class1.get_teachers())
