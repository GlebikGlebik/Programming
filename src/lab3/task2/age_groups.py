class Survey:
    def __init__(self):
        '''
        Инициализация переменных класса
        '''
        self.name_plus_age = []
        self.res = ''
        self.groups = []
        self.age_groups = {}

    def get_name_plus_age(self):
        """
        Данная функция выполняет считывание входных данных из файла 'input.txt' и записывает их в переменной 'name_plus_age', как 'массив массивов'
        для удобной работы с данными.
        """
        with open('input.txt', 'r', encoding='utf-8') as f:
            name_plus_age_input = f.read().split('\n')
            name_plus_age_input = [i.split(",") for i in name_plus_age_input if i != '']
            self.name_plus_age = dict(name_plus_age_input)
            self.name_plus_age = list([int(k), v] for v, k in self.name_plus_age.items())
            return self.name_plus_age

    def get_age_groups(self):
        """
        Данная функция сортирует респондентов по их возрастным группам и добавляет полученные данные в словарь 'age_groups', где key - это возрастная группа,
        а value - список кортежей, где каждый кортеж содержит имя и возраст участника. Также данная функция сортирует возрастные группы.
        """
        for j in self.groups:
            for age, name in self.name_plus_age:  # Разбитие списка всех респондентов на возрастные группы
                if age <= j == self.groups[0]:
                    self.age_groups[f'0-{j}'] = []
                elif age > j == self.groups[-1]:
                    self.age_groups[f'{j}+'] = []
                elif age <= j:
                    self.age_groups[f'{self.groups[self.groups.index(j) - 1] + 1}-{j}'] = []

        for i in self.groups:
            for age, name in self.name_plus_age:  # Разбитие списка всех респондентов на возрастные группы
                if age <= i == self.groups[0]:
                    self.age_groups[f'0-{i}'].append((name, age))
                elif age > i == self.groups[-1]:
                    self.age_groups[f'{i}+'].append((name, age))
                elif self.groups[self.groups.index(i) - 1] < age <= i:
                    self.age_groups[f'{self.groups[self.groups.index(i) - 1] + 1}-{i}'].append((name, age))

        for group in self.age_groups:
            self.age_groups[group] = sorted(self.age_groups[group], key=lambda x: (-int(x[1]), x[0]))  # Сортировка возрастных групп

        return self.age_groups

    def printer(self):
        """
        Данная функция задает формат вывода и создает результирующую строку, в которую записывается отформатированный вывод.
        """
        res = ''
        for group, respondents in self.age_groups.items():
            if respondents:
                string = ''
                for name, age in respondents:
                    string += f"{name} ({age}), "
                res += f"{group}: {string[:-2]} \n"
        return res

    def result(self):
        """
        Данная функция задает порядок выполнения методов класса.
        """
        self.name_plus_age = self.get_name_plus_age()
        self.age_groups = self.get_age_groups()
        self.res = self.printer()
        return self.res


def main():
    """
    В данной функции инициализируется экземпляр класса и вызывается результирующая функция класса.
    """
    kino = Survey()
    kino.groups = list(map(int, input().split()))
    res = kino.result()
    print(res)

if __name__ == "__main__":
    main()
