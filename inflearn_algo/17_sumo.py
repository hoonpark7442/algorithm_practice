# 섹션4. 이분탐색(결정알고리즘) & 그리디 알고리즘
# 6. 씨름선수(그리디)

# 내생각
# 일단 키로 정렬(키 큰 순으로). 그러면 키 1등인 애는 일단 합격. 그 다음 애부터 위의 애랑 몸무게 비교. 


# 문제풀이
# 위의 내 생각대로 하면 된다. 하지만 몸무게 비교할 때 어떻게 할 것인가? 이중포문? 노노. largest 변수에 몸무게 담아가며 비교해라

n=int(input())
body=[]
for i in range(n):
	a, b = map(int, input().split())
	body.append((a,b))

body.sort(reverse=True)
largest=0
cnt=0
for x, y in body:
	if y>largest:
		largest=y
		cnt+=1

print(cnt)
