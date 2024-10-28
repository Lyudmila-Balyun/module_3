def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a=0, b=25)
print_params(c=[1, 2, 3])

values_list = [8800, 'пять-пять-пять', (35, 35)]
values_dict = {'a': 'ЧСС', 'b': 120, 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [101, 'ОЧко']
print_params(*values_list_2, 42)

