def generate(numRows):
    ans = []

    for i in range(numRows):
        if(i == 0):
            ans.insert(i,[1])
        else:
            row = [1,1]
            for j in range(1,i):
                row.insert(j,ans[i-1][j-1] + ans[i-1][j])
            ans.insert(i,row)

    return ans


print(generate(numRows = 1))
print(generate(numRows = 2))
print(generate(numRows = 3))
print(generate(numRows = 4))
print(generate(numRows = 5))
print(generate(numRows = 30))