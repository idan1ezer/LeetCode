def romanToInt(s):
    if (len(s) > 15 or len(s) < 1):
        return 0

    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0

    for i in range(len(s)-1):
        if(dic[s[i]] >= dic[s[i+1]]):
            ans += dic[s[i]]
        else:
            ans -= dic[s[i]]

    return ans + dic[s[-1]]


print(romanToInt(s = "III"))
print(romanToInt(s = "IV"))
print(romanToInt(s = "IX"))
print(romanToInt(s = "LVIII"))
print(romanToInt(s = "MCMXCIV"))