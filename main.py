# "How many 3-digit numbers are there where the sum of the three digits is 10?"

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
valid_nums = []
some_of_digits = 0

for i in range(100, 1000):
    sum_of_digits = 0

    for digit in str(i):
        sum_of_digits += int(digit)

    if sum_of_digits == 10:
        valid_nums.append(i)

print(len(valid_nums))
print(valid_nums)


