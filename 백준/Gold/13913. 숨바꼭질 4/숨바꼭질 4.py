from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 100001
dist = [-1] * MAX
dist[N] = 0
parent = [-1] * MAX

q = deque([N])
while q:
    x = q.popleft()
    if x == K:
        print(dist[K])
        break
    
    for nx in [x-1, x+1, 2*x]:
        # 범위 안이고, 방문한 적이 없으면
        if 0 <= nx < MAX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
            # 무조건 먼저 도달한게 최단경로. 처음 도달했을때만 parent를 업데이트
            parent[nx] = x

# 경로 복원
path = []
cur = K

while cur != -1:
    path.append(cur)
    cur = parent[cur]

path.reverse()
print(*path)