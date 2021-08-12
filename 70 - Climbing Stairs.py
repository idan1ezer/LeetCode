def climbStairs(n):
    if (n > 45 or n < 1):
        return 0

    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(climbStairs(n = 1))
print(climbStairs(n = 2))
print(climbStairs(n = 3))
print(climbStairs(n = 4))