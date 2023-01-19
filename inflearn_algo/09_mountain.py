# 섹션3. 탐색&시뮬레이션
# 9. 봉우리

# 내 생각
# 메모이제이션? 일단 arr[1][1]부터 시작하겠지 그럼 arr[0][1], arr[1][0], arr[2][1], arr[1][2] 이렇게고
# i를 -1, +1해서 돌리고 j를 -1, +1해서 돌리고..
# 메모이제이션이 되었음 좋겠는데 이건 어케해야 될지 모르겠다..

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# a.insert(0, [0]*n)
# a.append([0]*n)

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# for x in a:
# 	x.insert(0, 0)
# 	x.append(0)

# cnt = 0

# for i in range(1, n+1):
# 	for j in range(1, n+1):
# 		if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
# 			cnt += 1

# print(cnt)


# 2회독차. 내 문제 풀이

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.append([0]*n)
a.insert(0, [0]*n)

for i in a:
	i.append(0)
	i.insert(0, 0)	

c = [-1,1,1,-1]
cnt=0

for i in range(1, n+1):
	for j in range(1, n+1):
		if a[i][j] > a[i+c[0]][j] and a[i][j] > a[i][j+c[1]] and a[i][j] > a[i+c[2]][j] and a[i][j] > a[i][j+c[3]]:
			print(a[i][j])
			cnt += 1

print(cnt)







































