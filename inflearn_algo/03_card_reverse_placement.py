# 섹션3. 탐색&시뮬레이션
# 3. 카드 역배치

# 대충 풀이

# arr = []
# for i in range(1,21):
# 	arr.append(i)

# for _ in range(10):
# 	temp = [0]*20
# 	start_idx, end_idx = map(int, input().split())
# 	cnt = start_idx-1

# 	for i in range(end_idx-1, start_idx-2, -1):
# 		temp[cnt] = arr[i]
# 		cnt +=1
	
# 	for i in range(start_idx-1, end_idx):
# 		arr[i] = temp[i]

# print(arr)

# 문제풀이

# a = list(range(21))

# for _ in range(10):
# 	s, e = map(int, input().split())

# 	for i in range((e-s+1)//2):	# swap을 할건데 반복을 e에서 s뺀거에 1 더하고 2로 나눈 몫 만큼만 돌면 된다.
# 		a[s+i], a[e-i] = a[e-i], a[s+i]

# a.pop(0)

# for x in a:
# 	print(x, end=' ')




# a =list(range(21))

# for _ in range(10):
# 	s, e = map(int, input().split())

# 	for i in range((e-s+1)//2):
# 		a[s+i], a[e-i] = a[e-i], a[s+i]
	
# a.pop(0)

# print(a)


# 5 10
# 9 13
# 1 2
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20

# 2회독차. 내 문제 풀이

# 요 부분 리스트로 받는 방법으로 수정!!
# arr=[]
# for i in range(21):
# 	arr.append(i)

arr=list(range(21))

for _ in range(10):
	s, e = map(int, input().split())
	
	for j in range(((e-s)//2)+1):
		arr[s+j], arr[e-j] = arr[e-j], arr[s+j]


arr.pop(0)

print(arr)




































