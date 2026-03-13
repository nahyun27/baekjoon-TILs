import sys
sys.setrecursionlimit(500 * 500 + 10) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

# DFS + 메모이제이션
# "순서를 모르겠으면, 필요할 때 재귀로 계산하자"
# "순서를 모르겠다" 싶으면 탑다운으로 전환

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

def dfs(i, j): # 메모이제이션
    if i == n - 1 and j == m - 1: # 목적지 도착
        return 1 # 경로 1개 발견
    if dp[i][j] != -1: # 이미 계산했으면 반환
        return dp[i][j]
    
    dp[i][j] = 0 # 계산 안했으면 경로 개수 0으로 표시하고 계산 시작
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우 탐색
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] < grid[i][j]: # 범위 안이고, 내리막이면
            dp[i][j] += dfs(ni, nj) # 경로 개수 더하기
    
    return dp[i][j]

print(dfs(0, 0))