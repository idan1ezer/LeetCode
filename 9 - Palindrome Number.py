def isPalindrome(x):
    if ((x < 0) or (x > pow(2, 31) - 1)):
        return False

    string = str(x)
    for i in range(len(string)):
        if(string[i] != string[len(string)-i-1]):
            return False
    return True


print(isPalindrome(x = 121))
print(isPalindrome(x = -121))
print(isPalindrome(x = 10))
print(isPalindrome(x = -101))