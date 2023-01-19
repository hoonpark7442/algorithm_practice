# 섹션4. 이분탐색(결정알고리즘) & 그리디 알고리즘
# 3. 뮤직비디오(결정알고리즘)

# 내 생각
# 두번째 줄에 곡 길이 주어진거 다 합친다. 그럼 45
# lt는 1 rt는 45로 해서 중간값 23분을 mid로 해둔다.
# 곡 길이 배열을 인덱스0부터 차례로 더하면서 23분 되면 카운팅, 그다음 인덱스부터 23될때까지 카운팅...
# 만약 m을 넘어서면 그땐 lt를 늘리고 m 안쪽으로 들어오면 일단 res에 23분 담고 rt=mid-1 해서 다시 돌림

def Count(capa):
	cnt=1
	sum=0
	for x in music:
		if sum+x > capa:
			cnt+=1
			sum=x
		else:
			sum+=x
	return cnt

n, m = map(int, input().split())
music = list(map(int, input().split()))
lt=1
rt=sum(music)
res=0
mx = max(music)

while lt <=rt:
	mid = (lt+rt)//2
	if mid >= mx and Count(mid) <= m:
		res = mid
		rt = mid-1
	else:
		lt = mid+1

print(res)