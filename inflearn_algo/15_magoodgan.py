# 섹션4. 이분탐색(결정알고리즘) & 그리디 알고리즘
# 4. 마구간 정하기

# 흠 모르겠다...
# 일단 정렬은 했음
# lt를 1, rt를 9로 생각했었는데 대충 맞았네

def Count(len):
	cnt = 1
	ep=Line[0]
	for i in range(1, n):
		if Line[i]-ep>=len:
			cnt+=1
			ep=Line[i]
	return cnt

n, c = map(int, input().split())
Line=[]

for _ in range(n):
	tmp=int(input())
	Line.append(tmp)

Line.sort()
lt=1
rt=Line[n-1]

while lt <= rt:
	mid=(lt+rt)//2
	if Count(mid)>=c:
		res = mid
		lt=mid+1
	else:
		rt=mid-1

print(res)
