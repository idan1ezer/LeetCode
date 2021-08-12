def lengthOfLastWord(s):
    newLst = s.split(" ")
    last = -1

    if (len(newLst) < 1):
        return 0
    while(len(newLst[last]) == 0 and abs(last) < len(newLst)):
        last -= 1
    return len(newLst[last])

print(lengthOfLastWord(s = "Hello World"))
print(lengthOfLastWord(s = " "))