class MovieRecommendation:
    def __init__(self):
        '''
        Инициализация переменных класса
        '''
        self.film_id = ''
        self.users_history = []
        self.main_user_history = [] #input("Введите id фильмов:",).split(',')
        self.film_name = ''

    def films(self):
        """
        Данная функция вывод название рекомендуемого фильма из файла 'films' по его id
        """
        with open('films.txt', 'r', encoding='utf-8') as f:
            films_input = f.read().split('\n')
            films_input = [i.split(",") for i in films_input if i != '']
            films = dict(films_input)
            if self.film_id == '':
                self.film_name = "Подходящих рекомендаций для пользователя нет"
            else:
                self.film_name = films[self.film_id]

        return self.film_name

    def history_of_watch(self):
        """
        Данная функция считывает глобальную историю просмотров из файла 'users'
        """
        with open("users.txt", 'r') as f:
            users_history_input = f.read().split('\n')
            for i in users_history_input:
                if i != '':
                    self.users_history.append(i.split(','))
            self.users_history = [set(i) for i in self.users_history]
            self.users_history = [list(i) for i in self.users_history]

        return self.users_history

    def find_film_id(self):
        """
        Данная функция подбирает рекомендуемый фильм для пользователя на основе его истории просмотров и общей истории просмотров среди всех пользователей сервиса
        """
        suitable_history = []
        for i in self.users_history:
            count = 0
            for j in range(len(i)):
                if i[j] in self.main_user_history:
                    count += 1
            if count >= (len(self.main_user_history) // 2):
                for k in i:
                    if k not in self.main_user_history:
                        suitable_history.append(k)

        mx_count = 0
        self.film_id = ''

        for j in set(suitable_history):
            count2 = suitable_history.count(j)
            if count2 > mx_count:
                mx_count = count2
                self.film_id = j

        return self.film_id

    def result(self):
        """
        Данная функция задает порядок выполнения методов класса.
        """
        self.history_of_watch()
        self.find_film_id()
        return self.films()

def main():
    """
    В данной функции инициализируется экземпляр класса и вызывается результирующая функция класса.
    """
    user = MovieRecommendation()
    res = user.result()
    print(res)

if __name__ == "__main__":
    main()