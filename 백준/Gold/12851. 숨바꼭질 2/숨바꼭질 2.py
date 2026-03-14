from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 100001
count = [0] * MAX
dist = [-1] * MAX
dist[N] = 0
count[N] = 1

q = deque([N])
while q:
    x = q.popleft()
    for nx in [x-1, x+1, 2*x]:
        # 범위 안이고, 방문한 적이 없으면
        if 0 <= nx < MAX: 
            # 처음 방문
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                count[nx] = count[x]
                q.append(nx)
            # 이미 방문한 적이 있는데, 거리가 같으면
            elif dist[nx] == dist[x] + 1:
                count[nx] += count[x]
    
print(dist[K])
print(count[K]) 