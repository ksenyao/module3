# 1
def print_params(a, b, c):
    print(a, b, c)


def print_params(*args):
    print(args)


list_ = [1, 'строка', True]
print_params(list_, 25, [123])
print_params(10, 'l', list_)
print_params(2, True, False)
print_params(*list_)
print_params()


# 2
def print_params(a, b, c):
    print(a, b, c)


values_list = ['apple', 3.14, (1, 2, 3)]
values_dict = {'a': 3.14, 'b': 'apple', 'c': (1, 2, 3)}
print_params(*values_list)

print_params(**values_dict)

# 3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
