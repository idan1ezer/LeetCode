def strStr(haystack, needle):
    if (len(needle) == 0):
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

print(strStr(haystack = "hello", needle = "ll"))
print(strStr(haystack = "aaaaa", needle = "bba"))
print(strStr(haystack = "", needle = ""))