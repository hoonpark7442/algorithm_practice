# 섹션4. 이분탐색(결정알고리즘) & 그리디 알고리즘
# 9. 증가수열 만들기(그리디)

# 내 생각
# 리스트에서 앞뒤 비교 후 작은 값 빼내고 결과리스트에 값 넣기 + 문자열결과리스트에 L,R 넣기
# 빼내기 전에 결과리스트 맨 뒤 값이랑 비교해서 더 커야 뺄 수 있다.

# 문제풀이
n=int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=''
tmp=[]

while lt<=rt:
	if a[lt]>last:
		tmp.append((a[lt],'L'))
	if a[rt]>last:
		tmp.append((a[rt],'R'))

	tmp.sort()
	if len(tmp) == 0:
		break
	else:
		res=res+tmp[0][1]
		last=tmp[0][0]
		if tmp[0][1]=='L':
			lt+=1
		else:
			rt-=1
	tmp.clear()

print(len(res))
print(res)