from collections import deque

# my_stack = deque(input().split())

# print(''.join(reversed(my_stack)))

my_stack = deque(input().split())
my_stack.reverse()

print(' '.join(my_stack))