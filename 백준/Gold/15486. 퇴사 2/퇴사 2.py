import sys
input = sys.stdin.readline
n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]

# dp[i] = i일째부터 퇴사일까지 얻을 수 있는 최대 수익
dp = [0] * (n + 2)

for i in range(n, 0, -1):
    t, c = schedule[i-1]
    if i + t <= n + 1:    # 일이 퇴사 전에 끝나는 경우
        dp[i] = max(dp[i+1], dp[i+t] + c) # 이 일을 했을때의 이득 업데이트
    else:
        dp[i] = dp[i + 1] 

print(dp[1])