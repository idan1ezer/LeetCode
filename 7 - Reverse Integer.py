def reverse(x):
    if (x == 0):
        return 0

    ans = 0
    leadZero = True
    negative = x < 0

    while (leadZero):
        if (x % 10 == 0):
            x = x // 10
        else:
            leadZero = False

    x = abs(x)
    for i in range(len(str(x))):
        add = x % 10
        ans += add * (10 ** (len(str(x)) - 1))
        x = x // 10
        if ((ans < pow(-2, 31)) or (ans > pow(2, 31) - 1)):
            return 0
    if negative:
        ans *= -1
    return ans

print(reverse(x = 123))
print(reverse(x = -123))
print(reverse(x = 120))
print(reverse(x = 0))