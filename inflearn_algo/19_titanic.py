# 섹션4. 이분탐색(결정알고리즘) & 그리디 알고리즘
# 8. 침몰하는 타이타닉(그리디)

# 내 생각
# 흠...몸무게 젤 많은 순으로 정렬 후 옆 인덱스랑 더한 값을 M이랑 비교. 넘어서면 그 다음 인덱스값 더해보고, 또 그다음 더해보고 이런식으로..?

# 문제풀이
# 흠 내 생각과 다르다. 내가 틀린듯.. 정렬해서 맨 앞 뒤 값 더해서 m이랑 비교

# n, limit = map(int, input().split())
# p = limit(map(int, input(),split()))
# p.sort()
# cnt=0
# while p:
# 	if len(p)==1:
# 		cnt+=1
# 		break
# 	if p[0]+p[-1]>limit:
# 		p.pop()
# 		cnt+=1
# 	else:
# 		p.pop(0)
# 		p.pop()
# 		cnt+=1

# print(cnt)

# 근데 list는 맨앞빼면 데이터 다 앞으로 옮기는 연산이 들어감. dequeue는 안그런다.

from collections import deque

n, limit = map(int, input().split())
p = limit(map(int, input(),split()))
p.sort()
p=deque(p)
cnt=0
while p:
	if len(p)==1:
		cnt+=1
		break
	if p[0]+p[-1]>limit:
		p.pop()
		cnt+=1
	else:
		p.popleft
		p.pop()
		cnt+=1

print(cnt)