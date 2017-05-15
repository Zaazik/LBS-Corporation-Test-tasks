from operator import itemgetter

AGE = 'age'
SEX = 'sex'
SECOND_NAME = 'second_name'
FIRST_NAME = 'first_name'
SORT_BY_FIELD = AGE
DEF_PREFIX = {
    'М': 'Г-н',
    'Ж': 'Г-жа',
}

data = [
    {FIRST_NAME: "Иван", SECOND_NAME: "Петров", SEX: "М", AGE: "34"},
    {FIRST_NAME: "Сергей", SECOND_NAME: "Терехов", SEX: "М", AGE: "25"},
    {FIRST_NAME: "Александра", SECOND_NAME: "Кац", SEX: "Ж", AGE: "23"},
    {FIRST_NAME: "Семен", SECOND_NAME: "Бурденко", SEX: "М", AGE: "25"},
]


def transform_data(func):
    def tmp(persons):
        persons = sorted(persons, key=itemgetter(SORT_BY_FIELD))
        for person in persons:
            data_for_print = [DEF_PREFIX[person[SEX]], person[FIRST_NAME], person[SECOND_NAME]]
            func(data_for_print)

    return tmp


@transform_data
def some_function(data_for_print):
    print(str.join(' ', data_for_print))

some_function(data)
