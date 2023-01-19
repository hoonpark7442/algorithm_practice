# 섹션3. 탐색&시뮬레이션
# 10. 스도쿠 검사

# 내 생각
# - 이중포문 돌면서..? 배열하나두고.. 1부터 9까지 값 넣는데 만약 들어가 있으면 그건 바로 no
# - 음 근데 3*3 여기는 어케..?

# def check(a):
# 	for i in range(9):
# 		ch1=[0]*10
# 		ch2=[0]*10
# 		for j in range(9):
# 			ch1[a[i][j]] = 1
# 			ch2[a[j][i]] = 1
# 		if sum(ch1) != 9 or sum(ch2) != 9:
# 			return False

# 	for i in range(3):
# 		for j in range(3):
# 			ch3=[0]*10
# 			for k in range(3):
# 				for s in range(3):
# 					ch3[a[i*3+k][j*3+s]]=1
# 			if sum(ch3) != 9:
# 				return False
# 	return True

# a = [list(map(int, input().split())) for _ in range(9)]
# if check(a):
# 	print("Yes")
# else:
# 	print("No")



# 1 4 3 6 2 8 5 7 9
# 5 7 2 1 3 9 4 6 8
# 9 8 6 7 5 4 2 3 1
# 3 9 1 5 4 2 7 8 6
# 4 6 8 9 1 7 3 5 2
# 7 2 5 8 6 3 9 1 4
# 2 3 7 4 8 1 6 9 5
# 6 1 9 2 7 5 8 4 3
# 8 5 4 3 9 6 1 2 7


# 2회독차. 내 문제 풀이

# a = [list(map(int, input().split())) for _ in range(9)]

# for i in range(9):
# 	temp=[0]*10
# 	temp2=[0]*10
# 	for j in range(9):
# 		temp[a[i][j]] = 1
# 		temp2[a[j][i]] = 1

# 	temp.pop(0)
# 	temp2.pop(0)
# 	for x in temp:
# 		if x == 0:
# 			print("NO")
# 			exit(0)

# 	for x in temp2:
# 		if x == 0:
# 			print("NO")
# 			exit(0)

# for i in range(9):
# 	for j in range(3):

# 실패실패실패실패실패실패실패실패실패실패실패실패실패실패실패실패실패실패실패실패







# def check(a):
# 	for i in range(9):
# 		ch1=[0]*10
# 		ch2=[0]*10
# 		for j in range(9):
# 			ch1[a[i][j]] = 1
# 			ch2[a[j][i]] = 1
# 		if sum(ch1) != 9 or sum(ch2) != 9:
# 			return False

# 	for i in range(3):
# 		for j in range(3):
# 			ch3=[0]*10
# 			for k in range(3):
# 				for s in range(3):
# 					ch3[a[i*3+k][j*3+s]]=1
# 			if sum(ch3) != 9:
# 				return False
# 	return True

# a = [list(map(int, input().split())) for _ in range(9)]
# if check(a):
# 	print("Yes")
# else:
# 	print("No")

def check(a):
	for i in range(9):
		ch1=[0]*10
		ch2=[0]*10
		for j in range(9):
			ch1[a[i][j]] = 1
			ch2[a[j][i]] = 1
		if sum(ch1) != 9 or sum(ch2) != 9:
			return False

	for i in range(3):
		for j in range(3):
			ch3=[0]*10
			for k in range(3):
				for s in range(3):
					ch3[a[i*3+k][j*3+s]]=1
			if sum(ch3) != 9:
				return False
	return True

a=[list(map(int, input().split())) for _ in range(9)]

if check(a):
	print("YES")
else:
	print("NO")





































