from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

tails = []
tails_idx = []   # tails 각 위치에 있는 원소의 원래 인덱스 (중복된 값이 있을 수도 있으니까.)
parent = [-1] * n  # parent[i] = arr[i]의 이전 원소 인덱스

for i, x in enumerate(arr):
    pos = bisect_left(tails, x)

    if pos == len(tails): 
        tails.append(x) # 현재 원소가 tails의 모든 원소보다 크면, tails의 맨 뒤에 추가
        tails_idx.append(i) # 현재 원소의 인덱스 추가
    else: 
        tails[pos] = x # 현재 원소가 tails의 어떤 원소보다 작거나 같으면, 해당 위치의 원소를 현재 원소로 교체
        tails_idx[pos] = i # 현재 원소의 인덱스로 교체

    # 이전 원소 기록 (pos > 0이면 바로 앞 위치의 원소가 predecessor)
    if pos > 0:
        parent[i] = tails_idx[pos - 1]

# 마지막 원소부터 역추적
path = []
cur = tails_idx[-1]
while cur != -1:
    path.append(arr[cur])
    cur = parent[cur]

path.reverse()

print(len(tails))
print(*path)