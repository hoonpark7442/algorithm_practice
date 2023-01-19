# 섹션4. 이분탐색(결정알고리즘) & 그리디 알고리즘
# 2. 랜선자르기(결정알고리즘)
# 이건 16_2110_router_installatioin.py 요거랑 같이 풀어보면 좋을거같다.

# 결정알고리즘 문제 특징은 우리가 찾고자 하는 값이 특정 범위 내에 있다는 것을 알 수 있다는 것.

def Count(len):
	cnt=0
	for x in Line:
		cnt+=(x//len)
	return cnt

k, n = map(int, input().split())
Line=[]
res=0
largest=0
for i in range(k):
	tmp=int(input())
	Line.append(tmp)
	largest=max(largest, tmp)

lt=1
rt=largest

while lt<=rt:
	mid=(lt+rt)//2
	if Count(mid) >= n:
		res = mid
		lt = mid+1
	else:
		rt=mid-1

print(res)