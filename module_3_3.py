def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(a = 3)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'моль', (1, 2)]
print_params(*values_list)

values_dict ={'a':3, 'b':'муха', 'c': ['а', 'б', 'в']}
print_params(**values_dict)

values_list_2 = [1, 'жук колорадский']
print_params(*values_list_2,42)