# https://www.acmicpc.net/problem/2920

num_list = list(map(int, input().split(' ')))

asc, desc = True, True

for i in range(1, 8):
	if num_list[i] > num_list[i-1]:
		desc = False
	elif num_list[i] < num_list[i-1]:
		asc = False

if asc:
	print("ascending")
elif desc:
	print("descending")
else:
	print("mixed")
