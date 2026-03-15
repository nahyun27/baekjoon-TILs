n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
parent = [-1] * n


for i in range(1, n):
    for j in range(i):
        # arr[i]보다 작은 원소들 중에서 dp[j]가 가장 긴 것을 선택하면 된다. (여태까지 가장 길게 모은 증가수열에 arr[i]를 붙인다.)
        if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            parent[i] = j

# 가장 긴 길이의 마지막 인덱스 찾기
last = dp.index(max(dp))

# 역추적
path = []
cur = last
while cur != -1:
    path.append(arr[cur])
    cur = parent[cur]

path.reverse()

print(max(dp))
print(*path)