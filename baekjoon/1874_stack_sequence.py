# https://www.acmicpc.net/problem/1874

n = int(input())

count = 1
stack = []
result = []
no_message = True
for i in range(1, n+1):
	data = int(input())

	while count <= data:
		stack.append(count)
		count += 1
		result.append('+')

	if stack[-1] == data:
		stack.pop()
		result.append('-')
	else:
		no_message = False
		break

if no_message == False:
	print('No')
else:
	print('\n'.join(result))	
