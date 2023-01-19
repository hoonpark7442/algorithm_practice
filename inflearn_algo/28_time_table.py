# 섹션5. 자료구조 활용(스택,큐,해쉬,힙)
# 7. 교육과정 설계(큐)

# 흠.. 큐에 넣고 하나씩 꺼내면서 필수과목순서랑 비교하면 될거같긴한데...큐에서 뺄 때 예를들어 필수과목순서가 CBA라고 하면 CBA에 속하기만 하면 일단 다 뽑아서 문자열로 만들고 걔를 비교해서 틀리면 노..? 왜냐면 제대로 계획짜여져있으면 큐에넣고 뽑을 때
# 필수과목 순서대로 뽑힐테니까..?

from collections import deque

need=input()
n=int(input())
for i in range(n):
	plan=input()
	dq=deque(need)
	for x in plan:
		if x in dq:
			if x!=dq.popleft():
				print("#%d NO" %(i+1))
				break

	else:
		if len(dq)==0:
			print("#%d YES" %(i+1))
		else:
			print("#%d NO" %(i+1))