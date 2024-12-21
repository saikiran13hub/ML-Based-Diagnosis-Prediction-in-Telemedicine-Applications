def read_digit_matrices():
    digits = []
    for _ in range(3):
        row = input().strip()
        digits.append([row[i:i+3] for i in range(0, len(row), 3)])
    return digits

def get_number_matrices():
    number = []
    for _ in range(3):
        row = input().strip()
        number.append([row[i:i+3] for i in range(0, len(row), 3)])
    return number

def is_valid_toggle(original, target):
    diff = 0
    for i in range(3):
        for j in range(3):
            if original[i][j] != target[i][j]:
                diff += 1
                if diff > 1:
                    return False
    return True

def possible_numbers(digit_matrices, number_matrices):
    possible_nums = [[] for _ in range(len(number_matrices[0]))]
    for i in range(len(number_matrices[0])):
        original_digit = [row[i] for row in number_matrices]
        valid = False
        for j, digit in enumerate(digit_matrices):
            if original_digit == digit or is_valid_toggle(original_digit, digit):
                possible_nums[i].append(str(j))
                valid = True
        if not valid:
            return "Invalid"
    return possible_nums

def sum_possible_numbers(possible_nums):
    from itertools import product
    all_numbers = product(*possible_nums)
    return sum(int("".join(num)) for num in all_numbers)

digit_matrices = read_digit_matrices()
number_matrices = get_number_matrices()

possible_nums = possible_numbers(digit_matrices, number_matrices)
if possible_nums == "Invalid":
    print("Invalid")
else:
    print(sum_possible_numbers(possible_nums))
