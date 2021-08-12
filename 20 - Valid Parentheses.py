def isValid(s):
    queue = []
    dic = {')':'(',']':'[','}':'{'}

    for ch in s:
        if (ch in dic.values()):
            queue.append(ch)
        elif (ch in dic.keys()):
            if((not queue) or dic[ch] != queue.pop()):
                return False
        else:
            return False

    return (queue == [])

print(isValid(s = "()"))
print(isValid(s = "()[]{}"))
print(isValid(s = "(]"))
print(isValid(s = "([)]"))
print(isValid(s = "{[]}"))