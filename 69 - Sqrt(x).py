def mySqrt(x):
    ans = 0
    if(x == 0):
        return 0

    while(ans <= pow(2,31)-1):
        if (ans * ans == x):
            return ans
        if(ans * ans > x):
            return ans-1
        ans += 1


print(mySqrt(x = 4))
print(mySqrt(x = 8))
