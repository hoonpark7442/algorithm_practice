# 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
# 각 물건은 무게(w)와 가치(v)로 표현될 수 있음
# 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음. 

# 물건(i)  물건1  물건2  물건3  물건4  물건5
# 무게(w)   10    15		 20		 25		30 
# 가치(v)   10		 12		 10		 8		5

data_list = [(10,10),(15,12),(20,10),(25,8),(30,5)]

def get_max_value(data_list, capacity):
	data_list = sorted(data_list, key=lambda x:x[1]/x[0], reverse=True)
	total_value = 0
	details = list()

	for data in data_list:
		if capacity - data[0] >= 0:
			capacity -= data[0]
			total_value += data[1]
			details.append([data[0], data[1], 1])
		else:
			fraction = capacity / data[0]
			total_value += data[1] * fraction
			details.append([data[0], data[1], fraction])
			break

	return total_value, details


val = get_max_value(data_list, 30)
print(val)