import sys

string_list = list(sys.stdin.readline().strip())
bomb_list = list(sys.stdin.readline().strip())
stack = []

for char in string_list:
  stack.append(char)

  if len(stack) >= len(bomb_list):
    if stack[-len(bomb_list):] == bomb_list: # 폭파 대상 문자열 발견!
      for _ in range(len(bomb_list)):
        stack.pop()

if not stack:
  print('FRULA')
else:
  print(''.join(stack))