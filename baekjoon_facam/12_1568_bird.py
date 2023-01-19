# https://www.acmicpc.net/problem/1568
# 05. 기본 탐색 알고리즘 - 기초 문제풀이

# 어떻게 풀어야 할까 - 내 생각
# 문제 이해
# - 새의 수가 14라면, 1 일땐 한마리 날라가고(13마리남음), 2일땐 두마리 날라가고(11마리남음), ..., 5일때 보니 새가 4마리만 남음. 
# 그럼 다시 1부터, 1일때 4마리중 한마리, 2일때 3마리중 2마리, 3일땐 또 다시 1부터, 1마리 중 1마리. 
# 이렇게 7초가 걸린거임

# 내가 푼거
# birds = int(input())

# i = birds
# seconds = 0
# count = 1

# while birds > 0:
# 	if birds < count:
# 		count = 1
# 	else:
# 		birds -= count
# 		count += 1
# 		seconds += 1

# print(seconds)

# 핵심 아이디어
# - N이 최대 10억
# - K가 반복적으로 증가하므로 날아가는 새의 마리 수는 빠르게 증가
# - 따라서 문제에서 요구하는대로 단순히 구현하여 정답 처리 받을 수 있다.
# - 등차수열이므로 시간복잡도 O(n^2).. 모르겠다...

# 문제풀이
n = int(input())
result = 0
k = 1

while n != 0:
	if k > n:
		k = 1
	n -= k
	k += 1
	result += 1

print(result)
