from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if N >= K:
    print(N - K)
else:
    MAX = 100001
    visited = [-1] * MAX
    visited[N] = 0
    
    q = deque([N])
    while q:
        x = q.popleft()
        if x == K:
            print(visited[K])
            break
        
        for nx in [x-1, x+1, 2*x]:
            # 범위 안이고, 방문한 적이 없으면
            if 0 <= nx < MAX and visited[nx] == -1:
                # 0초짜리를 그냥 `append`하면 **나중에 처리**돼요. 근데 0초니까 **즉시 처리**해야 해요.
                if nx == 2*x:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)