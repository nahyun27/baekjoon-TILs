from bisect import bisect_left

n = int(input())
seq = list(map(int, input().split()))

tails = []

for x in seq:
    pos = bisect_left(tails, x)
    if pos == len(tails):
        tails.append(x)
    else:
        tails[pos] = x

print(len(tails))