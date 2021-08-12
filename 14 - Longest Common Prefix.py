def longestCommonPrefix(strs):
    if((len(strs) < 1) or (len(strs) > 200)):
        return False

    shortestWord = min(strs, key=len)

    for i, char in enumerate(shortestWord):
        for word in strs:
            if word[i] != char:
                return shortestWord[:i]
    return shortestWord

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["reflower","flow","flight"]))