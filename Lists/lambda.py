string_list = ['1', '2', '3', '4']
numbers = list(map(int, string_list))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
