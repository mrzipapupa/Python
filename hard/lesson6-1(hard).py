# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

from hard.Worker import Worker


def extract_worker_hours():
    with open("hours_of.txt", "r") as hours_of:
        hours = []
        collection = hours_of.readlines()[1:]
        for record in collection:
            attr = record.split()
            dict_of_hours = {}
            dict_of_hours["name"] = attr[0]
            dict_of_hours["surname"] = attr[1]
            dict_of_hours["hour"] = attr[2]
            hours.append(dict_of_hours)
    return hours


if __name__ == "__main__":
    hours = extract_worker_hours()
    with open("workers.txt", "r") as file_workers:
        workers = []
        iterator = 0
        collection = file_workers.readlines()[1:]
        for line in collection:
            workers.append(Worker(line))
            workers[iterator].set_worked_hours(hours)
            workers[iterator].set_coff_salary()
            workers[iterator].calculate_real_salary()
            print(workers[iterator].get_worker())
            iterator += 1
