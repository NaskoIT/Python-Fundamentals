nums = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in nums if x % 2 == 0]
print(even_numbers)

squares = [x ** 2 for x in even_numbers]
print(squares)

multiplied_list = squares * 3
print(multiplied_list)
