n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)

for i in range(0, length):
	for j in range(i+1, length):
		for k in range(j+1, length):
			data_sum = data[i] + data[j] + data[k]
			if data_sum <= m:
				result = max(result, data_sum)

print(result)