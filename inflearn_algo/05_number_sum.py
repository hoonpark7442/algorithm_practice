# 섹션3. 탐색&시뮬레이션
# 5. 수들의 합

# 내 풀이
# 시간복잡도가 n제곱이다. 안좋다.
# N이 총 1만개다. 즉 최악의 경우 1억번 탐색한다는거다. 이렇게 풀면 안된다.
# n, m = map(int, input().split())
# li = list(map(int, input().split()))

# result = 0

# for i in range(len(li)):
# 	if li[i] == m:
# 		result += 1
# 		continue
# 	sum_li = li[i]
# 	for j in range(i+1, len(li)):
# 		sum_li += li[j]

# 		if sum_li == m:
# 			result += 1
# 			break
# 		elif sum_li > m:
# 			break

# print(result)

# 문제풀이

# n, m = map(int, input().split())
# a=list(map(int, input().split()))
# lt=0
# rt=1
# tot=a[0]
# cnt=0

# while True:
# 	if tot < m:
# 		if rt<n:
# 			tot += a[rt]
# 			rt += 1
# 		else:
# 			break
# 	elif tot == m:
# 		cnt+=1
# 		tot-=a[lt]
# 		lt+=1
# 	else:
# 		tot-=a[lt]
# 		lt+=1

# print(cnt)



# 2회독차. 내 문제 풀이


# n,m = map(int, input().split())
# a = list(map(int, input().split()))

# p0, p1 = 0, 0

# size = len(a)

# res=0
# count=0

# while p1 < size:
# 	print("====")
# 	print("p0 = %s" % p0)
# 	print("p1 = %s" % p1)
# 	print("res = %s" % res)
# 	print("count = %s" % count)
# 	print("====")
# 	if p0 == p1:
# 		p1+=1
# 	elif res == 0:
# 		res = a[p0] + a[p1]
# 	elif res < m:
# 		p1+=1
# 	elif res == m:
# 		count += 1
# 		p0 += 1
# 		res=0
# 	elif res > m:
# 		res = 0
# 		p0 += 1

# print(count)

# 실패!!!!!!!!!!!!못풀겠다.

# n, m = map(int, input().split())
# a=list(map(int, input().split()))
# lt=0
# rt=1
# tot=a[0]
# cnt=0

# while True:
# 	if tot < m:
# 		if rt<n:
# 			tot += a[rt]
# 			rt += 1
# 		else:
# 			break
# 	elif tot == m:
# 		cnt+=1
# 		tot-=a[lt]
# 		lt+=1
# 	else:
# 		tot-=a[lt]
# 		lt+=1

# print(cnt)


n,m = map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0

while True:
	if tot < m:
		if rt < n:	# 이 부분에 rt < n 체크 하는게 들어오는게 중요할텐데 나중에 풀때 이 부분에 잘 적용할지 모르겠다...어느부분에 적용할지 헷갈릴거같은디..
			tot += a[rt]
			rt += 1
		else:
			break
	elif tot == m:
		cnt+=1
		tot -= a[lt]
		lt += 1
	else:
		tot -= a[lt]
		lt += 1

print(cnt)





































