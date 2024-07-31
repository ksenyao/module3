def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
print_params()

# 2
values_list = ['apple', 3.14, (1, 2, 3)]
values_dict = {'a': 3.14, 'b': 'apple', 'c': (1, 2, 3)}
print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)