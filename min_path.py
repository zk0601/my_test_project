# 最短路径和，第一行走到最后一行，而且只能向下或者斜向下走
array = [[1,8,5,2],
         [4,1,7,3],
         [3,6,2,9]]

x = len(array[0])
y = len(array)

dp = [[0 for i in range(x)] for j in range(y)]

for i in range(y):
    for j in range(x):
        if i == 0:
            dp[i][j] = array[i][j]
        if j == 0:
            dp[i][j] = array[i][j] + min(dp[i-1][j], dp[i-1][j+1])
        elif j == x-1:
            dp[i][j] = array[i][j] + min(dp[i-1][j], dp[i-1][j-1])
        else:
            dp[i][j] = array[i][j] + min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1])

print(min(dp[-1]))