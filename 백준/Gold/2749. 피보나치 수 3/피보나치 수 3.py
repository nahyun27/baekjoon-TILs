# 10^6 = 10^k 꼴에서 피사노 주기는 15 × 10^(k-1)
# 모르면 아래와 같이 찾기
# a, b = 0, 1
# for i in range(1, MOD*MOD):
#     a, b = b, (a + b) % MOD

#     if a == 0 and b == 1:
#         print(i)
#         break
n = int(input())
n %= 1500000

a, b = 0, 1
for _ in range(n):
    a, b = b, (a + b) % 1000000

print(a)