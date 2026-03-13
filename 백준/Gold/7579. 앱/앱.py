# 앱
import sys
sys.setrecursionlimit(500 * 500 + 10) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

# [난이도 9] M 바이트를 확보하기 위한 앱 비활성화의 최소의 비용 구하기 = knapsack (DP)
# 해당 문제가 최대 이익을 구하는 문제라고 해봤자
# 본질은 물건을 봉투에 넣느냐 마느냐에 관한 문제이다.

n, m = map(int, input().split()) # 앱 개수, 필요한 추가 메모리
bites = list(map(int, input().split())) # 각 앱의 바이트
costs = list(map(int, input().split())) # 각 앱의 비활성화 비용

dp = [0] * (sum(costs) + 1)
# DP가 하는 일: "비용 j를 쓰면 최대 얼마나 확보할 수 있어?" 를 모든 j에 대해 계산
# dp[j] = 비용 j를 썼을 때 확보 가능한 최대 메모리
# dp[j] >= M 을 만족하는 최소 j 찾기 !
for i in range(n): # 앱 i를 고려에 추가한다
    for j in range(sum(costs), costs[i] - 1, -1): # "비용 j를 쓸 때, 앱i를 버리면 이득인가?"
        # dp[j]  (i 안버림), dp[j - costs[i]] + bites[i] (비용 costs[i]는 앱i에 쓰고, 나머지 j - costs[i]는 다른 앱들에 씀, 비용 j-costs[i]를 썼을 때의 최대 메모리 + 앱i의 바이트)
        dp[j] = max(dp[j], dp[j - costs[i]] + bites[i]) 
        
print(min(j for j in range(sum(costs) + 1) if dp[j] >= m))