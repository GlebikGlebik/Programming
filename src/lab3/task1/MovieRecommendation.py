class MovieRecommendation:
    def __init__(self):
        self.film_id = ''
        self.users_history = []
        self.main_user_history = []
        self.film_name = ''

    def films(self):
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
        with open("users.txt", 'r') as f:
            users_history_input = f.read().split('\n')
            for i in users_history_input:
                if i != '':
                    self.users_history.append(i.split(','))
            self.users_history = [set(i) for i in self.users_history]
            self.users_history = [list(i) for i in self.users_history]

        return self.users_history

    def find_film_id(self):
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
        self.history_of_watch()
        self.find_film_id()
        return self.films()

def main():
    user = MovieRecommendation()
    user.main_user_history = input("Введите id фильмов:",).split(',')
    res = user.result()
    print(res)

if __name__ == "__main__":
    main()