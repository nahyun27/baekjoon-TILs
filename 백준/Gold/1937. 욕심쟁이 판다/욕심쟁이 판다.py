import sys
sys.setrecursionlimit(500 * 500 + 10) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

# [난이도 5] 판다가 이동할 수 있는 칸수의 최댓값 (목적지 없음)
# DFS + 메모이제이션

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

def dfs(i, j): # 메모이제이션
    if dp[i][j] != -1: # 이미 계산했으면 반환
        return dp[i][j]
    
    dp[i][j] = 1 # 계산 안했으면 경로 개수 0으로 표시하고 계산 시작
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우 탐색
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > grid[i][j]: # 범위 안이고, 대나무가 더 많으면
            dp[i][j] = max(dp[i][j], 1 + dfs(ni, nj))
            continue
    
    return dp[i][j]


print(max(dfs(i, j) for i in range(n) for j in range(n)))
