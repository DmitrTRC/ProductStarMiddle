from functools import reduce

if __name__ == '__main__':

    print('Task 1')

    arr_1 = [i for i in range(5, 15)]

    arr_2 = arr_1[::2]

    multiplication = reduce(lambda x, y: x * y, arr_2)

    summ = reduce(lambda x, y: x + y, arr_2)

    result_arr = list(arr_2)

    result_arr.append(multiplication)
    result_arr.append(summ)

    result_arr.sort(reverse = True)

    array_of_string = list(map(str, result_arr))

    result = '='.join(array_of_string)

    print(result)

    print('Task 2')

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 5, 9, -7, -10]

    print(list(filter(lambda x: x < 5, a)))

    print('Task 3')

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11]

    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 11, 12, 13]

    result = sorted(set((filter(lambda x: x in b, a))))

    print(result)

    print('Task 4')

    s = 'kafka python course stack flow dict list python stack course star product star product analytics flow star ' \
        'kafka stack flow ython list set ist fit predict dict list python ourse ython ourse star product ist fit ' \
        'predict analytics kafka stack flow product ist fit predict analytics star flow dict flow list python course ' \
        'stack flow dict list python stack course'

    words = sorted(s.split(' '))

    from collections import Counter

    c = Counter(words).most_common(1)

    print(c)

    print('Task 5')

    names = ['igor', 'dasha', 'martin', 'vladimir', 'rishat', 'maria', 'marat', 'petr', 'dima', 'polina', 'katya',
             'elena']

    occupations = ['smm', 'developer', 'analyst', 'president', 'analyst', 'ceo', 'customer development', 'founder',
                   'developer', 'ml engineer', 'product manager', 'cmo']

    result = dict(zip(names, occupations))

    print(result.get('maria'))

    print('Task 6')

    dict1 = {1: 10, 2: 20, 3901: 11, 384: 13, 8489: 1, 48: 10}

    dict2 = {3: 30, 4: 40, 93: 12, 91: 41, 95: 1, 841: 11, 584: 11}

    dict3 = {5: 50, 6: 60, 9: 90, 3: 13, 7: 11}

    dict4 = {**dict1, **dict2, **dict3}

    c = Counter(dict4.values()).most_common(1)

    print(dict4.__len__(), c[0][0], sep = ',')

    print('Task 7')


    def get_symbol_count(string: str) -> dict:
        return dict(Counter(string))


    def get_8_less_popular_symbols(string: str) -> list:
        return sorted(get_symbol_count(string).items(), key = lambda x: x[1])[:8]


    given_string = 'Python Star Course for beginners and experts for data science and analytics without sql with code'

    print(get_symbol_count(given_string))

    less_sym = get_8_less_popular_symbols(given_string)

    for sym, occur in less_sym:
        print(f'{sym}', end = '')
