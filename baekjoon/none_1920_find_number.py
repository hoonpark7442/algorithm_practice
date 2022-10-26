# https://www.acmicpc.net/problem/1920

n = int(input())
arr = set(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
	if i in arr:
		print(1)
	else:
		print(0)