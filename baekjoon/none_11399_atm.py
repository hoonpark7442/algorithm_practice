# greedy

N = 5
N_list = [3,1,4,3,2]
minimum = 0

N_list.sort()

for index in range(N):
	for index2 in range(index+1):
		minimum += N_list[index2]

print(minimum)