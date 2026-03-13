# "교차 불가" 같은 강한 순서 제약이 있으면
# → 그리디 우선 고려: 위→아래 순으로 하나씩 연결을 시도하면 최적이 보장
import sys
sys.setrecursionlimit(10000 * 500 + 10)
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

def dfs(x, y):
    if y == C - 1:
        return True

    visited[x][y] = True
    # 최적 보장: 위에서부터 시작하기 때문에, DFS도 위쪽 경로를 먼저 선택해야 나중 파이프에게 아래쪽 경로를 양보할 수 있어요.
    for dx in [-1, 0, 1]:
        nx, ny = x + dx, y + 1
        if 0 <= nx < R and grid[nx][ny] == '.' and not visited[nx][ny]:
            if dfs(nx, ny):
                return True
    return False

ans = 0
# 0번째 열에서 시작해서 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 이동
# 마지막 열에 도착하면 True 반환
for i in range(R): # 0번째 열의 모든 칸을 검사하면서
    if dfs(i, 0): # 파이프를 설치할 수 있으면
        ans += 1 # 파이프 개수 증가
print(ans)