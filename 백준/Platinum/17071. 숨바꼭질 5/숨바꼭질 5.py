from collections import deque

N, K = map(int, input().split())

MAX = 500001
# visited[0][P] = P를 짝수 시간에 밟을 수 있는가
# visited[1][P] = P를 홀수 시간에 밟을 수 있는가
visited = [[False] * MAX for _ in range(2)]
visited[0][N] = True

q = deque([(N, 0)])

while q:
    pos, sec = q.popleft()
    # 등차수열 합 공식! 만큼 동생의 위치 변함
    brother_pos = K + sec * (sec + 1) // 2
    # 동생이 범위를 벗어났으면 종료
    if brother_pos > 500000:
        print(-1)
        break
    # 수빈이가 t와 같은 홀짝으로 현재 동생 위치에 도달한 적 있으면
    # 그 이후 제자리 반복으로 정확히 t초에 동생 위치에 있을 수 있음
    if visited[sec % 2][brother_pos]:
        print(sec)
        break
      
    # 현재 레벨(시간 t)의 노드만 처리 (한 depth 후에 동생위치 업데이트해야하므로)
    for npos in [pos-1, pos+1, 2*pos]:
        if 0 <= npos < MAX and not visited[(sec+1) % 2][npos]:
            visited[(sec+1) % 2][npos] = True
            q.append((npos, sec+1))