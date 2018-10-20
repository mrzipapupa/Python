class Worker:
    def __init__(self, file_string):
        self._args = file_string.split()
        self._name = self._args[0]
        self._surname = self._args[1]
        self._salary = int(self._args[2])
        self._position = self._args[3]
        self._hours_norm = int(self._args[4])
        self._hours_real = 0
        self._coff_salary = 0.0
        self._real_salary = 0.0

    def set_worked_hours(self, collection):
        for record in collection:
            if self._name == record.get("name") and self._surname == record.get("surname"):
                self._hours_real = record.get("hour")

    def set_coff_salary(self):
        self._coff_salary = self._salary / self._hours_norm

    def calculate_real_salary(self):
        hours_real = int(self._hours_real)
        different_hours = abs(self._hours_norm - hours_real)
        if hours_real < self._hours_norm:
            self._real_salary = self._salary - (different_hours * self._coff_salary)
        else:
            self._real_salary = self._salary + (different_hours * self._coff_salary * 2)

    def get_worker(self):
        result = "{0} {1} получил зарплату {2}".format(self._surname, self._name, self._real_salary)
        return result