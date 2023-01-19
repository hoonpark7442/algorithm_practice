# 섹션4. 이분탐색(결정알고리즘) & 그리디 알고리즘
# 5. 미팅룸 배정(그리디)
# 그리디는 이 단계에서 가장 좋은 거 선택. 보통은 정렬을 한 다음 좋은거 선택. 

# 먼저 회의 끝나는 시간으로 정렬해라

n = int(input())
meeting=[]
for i in range(n):
	s, e = map(int, input().split())
	meeting.append((s,e))

meeting.sort(key=lambda x : (x[1], x[0]))

et=0
cnt=0
for s, e in meeting:
	if s >= et:
		et=e
		cnt+=1

print(cnt)
