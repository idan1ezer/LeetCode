def plusOne(digits):
    for i in reversed(range(len(digits))):
        if (digits[i] < 9):
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    digits.insert(0,1)
    return digits

print(plusOne(digits = [1,2,3]))
print(plusOne(digits = [4,3,2,1]))
print(plusOne(digits = [0]))
print(plusOne(digits = [9,9,9,9]))