def isPalindrome(s):
    newString = ""

    for c in s:
        if (c.isalnum()):
            newString += c.lower()

    if (newString != newString[::-1]):
        return False

    return True

print(isPalindrome(s = "A man, a plan, a canal: Panama"))
print(isPalindrome(s = "race a car"))
print(isPalindrome(s = "0P"))

