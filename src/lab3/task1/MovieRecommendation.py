class MovieRecommendation:
    @staticmethod
    def films(film_id):
        with open('films.txt', 'r', encoding='utf-8') as f:
            films_input = f.read().split('\n')
            films_input = [i.split(",") for i in films_input if i != '']
            films = dict(films_input)
            if film_id == '':
                film_name = "Подходящих рекомендаций для пользователя нет"
            else:
                film_name = films[film_id]

        return film_name

    @staticmethod
    def history_of_watch():
        with open("users.txt", 'r') as f:
            users_history_input = f.read().split('\n')
            users_history = []
            for i in users_history_input:
                if i != '':
                    users_history.append(i.split(','))
            users_history = [set(i) for i in users_history]
            users_history = [list(i) for i in users_history]

        return users_history

    @staticmethod
    def find_film_id(users_history, main_user_history):
        suitable_history = []

        for i in users_history:
            count = 0
            for j in range(len(i)):
                if i[j] in main_user_history:
                    count += 1
            if count >= (len(main_user_history) // 2):
                for k in i:
                    if k not in main_user_history:
                        suitable_history.append(k)

        mx_count = 0
        film_id = ''

        for j in set(suitable_history):
            count2 = suitable_history.count(j)
            if count2 > mx_count:
                mx_count = count2
                film_id = j

        return film_id

    @staticmethod
    def main(input_user):
        user = input_user
        users_history = MovieRecommendation.history_of_watch()
        film_id = MovieRecommendation.find_film_id(users_history, user)
        film_name = MovieRecommendation.films(film_id)
        return film_name

if __name__ == "__main__":
    main_user_history = input("Введите id фильмов:",).split(',')
    recommended_film = MovieRecommendation.main(main_user_history)
    print(recommended_film)