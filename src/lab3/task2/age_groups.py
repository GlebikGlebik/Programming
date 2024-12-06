class Survey:
    @staticmethod
    def get_name_plus_age():
        with open('input.txt', 'r', encoding ='utf-8') as f:
            name_plus_age_input = f.read().split('\n')
            name_plus_age_input = [i.split(",") for i in name_plus_age_input if i != '']
            name_plus_age = dict(name_plus_age_input)
            name_plus_age = list([int(k),v] for v,k in name_plus_age.items())
            return name_plus_age

    @staticmethod
    def get_age_groups(name_plus_age):
        age_groups = {
            '0-18': [],
            '19-25': [],
            '26-35': [],
            '36-45': [],
            '46-60': [],
            '61-80': [],
            '81-100': [],
            '101+': []
        }
        for age, name in name_plus_age:
            if age <= 18:
                age_groups['0-18'].append((name, age))
            elif age <= 25:
                age_groups['19-25'].append((name, age))
            elif age <= 35:
                age_groups['26-35'].append((name, age))
            elif age <= 45:
                age_groups['36-45'].append((name, age))
            elif age <= 60:
                age_groups['46-60'].append((name, age))
            elif age <= 80:
                age_groups['61-80'].append((name, age))
            elif age <= 100:
                age_groups['81-100'].append((name, age))
            else:
                age_groups['101+'].append((name, age))

        for group in age_groups:
            age_groups[group] = sorted(age_groups[group], key=lambda x: (-int(x[1]), x[0]))

        return age_groups

    @staticmethod
    def printer(age_groups):
        res = ''
        for group, respondents in age_groups.items():
            if respondents != []:
                string = ''
                for name, age in respondents:
                    string += f"{name} ({age}), "
                res += f"{group}: {string[:-2]} \n"
        return res

def main():
    name_plus_age = Survey.get_name_plus_age()
    age_groups = Survey.get_age_groups(name_plus_age)
    res = Survey.printer(age_groups)
    print(res)

if __name__ == "__main__":
    main()