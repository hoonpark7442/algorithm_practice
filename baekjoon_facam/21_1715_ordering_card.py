# https://www.acmicpc.net/problem/1715
# 08. 고급 탐색 알고리즘 - 핵심 유형 문제풀이
# 문제유형: 힙, 자료구조, 그리디

# 생각해보기

# (10+20)+(30+40) = 100
# (10+40)+(50+20) = 120
# (20+40)+(60+10) = 130

# 모르겠군...

# 문제 풀이 핵심 아이디어
# - 가장 크기가 작은 숫자카드 묶음들을 먼저 합쳤을 때 비교 횟수가 가장 적다.
# - 가장 크기가 작은 숫자 카드 묶음들을 2개씩 합치기 위해 힙자료구조를 이용

import heapq

n = int(input())
heap = []

for i in range(n):
	data = int(input())
	heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
	fir = heapq.heappop(heap)
	sec = heapq.heappop(heap)
	sum_val = fir + sec
	result += sum_val
	heapq.heappush(heap, sum_val)

print(result)









