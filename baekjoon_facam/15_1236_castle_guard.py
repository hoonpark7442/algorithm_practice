# https://www.acmicpc.net/problem/1236
# 05. 기본 탐색 알고리즘 - 기초 문제풀이

# 어떻게 풀어야 할까 - 내 생각

# 내 문제풀이 - 틀렸다고 나옴
# n, m = map(int, input().split())
# arr = []

# for _ in range(n):
# 	to_array = [char for char in input()]
# 	arr.append(to_array)

# result_arr = []

# check_bool = True

# for i in range(len(arr)):
# 	count_row = 0
# 	count_col = 0
# 	for j in range(len(arr[i])):
# 		if arr[i][j] == '.':
# 			count_row += 1

# 		if j >= n:
# 			continue
# 		elif arr[j][i] == '.': 
# 			count_col += 1
	
# 	if count_row == m or count_col == n:
# 		check_bool = False

# 	result_arr.append(count_row)
# 	result_arr.append(count_col)

# if check_bool:
# 	print(0)
# else:
# 	print(min(result_arr))

# 문제풀이 핵심 아이디어
# - 모든 행, 모든 열에 한 명 이상의 경비원이 있어야 한다
# - 행기준, 열기준으로 필요한 경비원 수를 각각 계산하여 더 큰 수를 출력한다.
# 그냥 비어있는 행이나 열을 찾아서 몇 개 비어있는지만 체크해서 최소값 출력하면 되나보다...

n, m = map(int, input().split())
arr = []

for _ in range(n):
	arr.append(input())

row = [0] * n
col = [0] * m

for i in range(n):
	for j in range(m):
		if arr[i][j] == 'X':
			row[i] = 1
			col[j] = 1

row_count = 0

for i in range(n):
	if row[i] == 0:
		row_count += 1

col_count = 0
for j in range(m):
	if col[j] == 0:
		col_count += 1

print(max(row_count, col_count))











