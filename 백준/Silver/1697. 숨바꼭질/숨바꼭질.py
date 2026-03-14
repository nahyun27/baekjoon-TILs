n, k = map(int, input().split())

# 순환을 할 수 있기 때문에 BFS를 사용한다.
# DP를 사용하려면 순서나 규칙을 정해줘야한다. (dp가 왼쪽->오른쪽으로만 정의되도록 제한해줘야함)
dp = [0] * (k+2)

if n >= k:
    print(n - k)
    
else: 
  for i in range(n):
    dp[i] = n - i

  for i in range(n+1, k+1):
      if i % 2 == 0:
          dp[i] = dp[i//2] + 1
      else:
          # 2를 더하는 이유는 (i+1)//2 와 (i-1)//2 는 i와 2칸 차이이기 때문
          dp[i] = min(dp[(i+1)//2], dp[(i-1)//2]) + 2
      dp[i] = min(dp[i], dp[i-1] + 1)

  print(dp[k])