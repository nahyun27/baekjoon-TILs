expression = input().strip()
priority = {'+': 1, '-': 1, '*': 2, '/': 2}
stack = []
result = []

for ch in expression:
    if ch.isalpha():
        result.append(ch)
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(': 
            result.append(stack.pop())
        stack.pop()
    else: # 연산자인 경우 일단은 스택에 넣는다. 
      # 단, 이미 스택에 연산자가 있다면, 우선순위가 더 높은 연산자를 먼저 꺼내고 넣는다.
      # 우선순위가 같으면 왼쪽에서 오른쪽으로 계산하므로, 
      while stack and stack[-1] != '(' and priority.get(stack[-1], 0) >= priority[ch]:
        result.append(stack.pop())
      stack.append(ch)

while stack:
    result.append(stack.pop())

print(''.join(result))