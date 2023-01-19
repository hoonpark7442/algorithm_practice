# 섹션3. 탐색&시뮬레이션
# 4. 두 리스트 합치기

# 내 풀이
# list1 = []
# list2 = []

# n = int(input())

# for _ in range(n):
# 	list1.append(int(input()))

# m = int(input())

# for _ in range(m):
# 	list2.append(int(input()))

# list3 = list1+list2

# list3.sort()

# print(list3)


# 문제풀이
# 걍 sort함수 쓰라는게 아니다. sort함수 시간복잡도는 O(nlogn)
# 입력되는 리스트가 이미 정렬되어 있으므로 O(n)으로 끝낼 수 있다.
# 문제풀이보니까 병합정렬에서 두 리스트 합치는 방법처럼 각 리스트에 포인터두고 비교해가면서 포인터 증가시키는 방식으로 푼다.

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))

# p1,p2 = 0, 0
# c = []

# while n > p1 and m > p2:
# 	if a[p1] <= b[p2]:
# 		c.append(a[p1])
# 		p1 += 1
# 	else:
# 		c.append(b[p2])
# 		p2 += 1

# if n > p1:
# 	c = c+a[p1:]

# if m > p2:
# 	c = c+b[p2:]

# for i in c:
# 	print(i, end=' ')



# 2회독차. 내 문제 풀이

n = int(input())
arr=list(map(int, input().split()))
m = int(input())
arr2=list(map(int, input().split()))

p1,p2 = 0, 0
c = []

while p1 < n and p2 < m:
	if arr[p1] < arr2[p2]:
		c.append(arr[p1])
		p1 += 1
	else:
		c.append(arr2[p2])
		p2+=1

if p1 < n:
	for i in range(p1, n):
		c.append(arr[i])

if p2 < m:
	for i in range(p2, m):
		c.append(arr2[i])


print(c)






































