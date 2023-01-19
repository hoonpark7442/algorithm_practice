# 섹션5. 자료구조 활용(스택,큐,해쉬,힙)
# 1. 가장 큰 수(스택)

# 모르겠다...아 열받아

# 문제풀이
# 5 2 7 6 8 2 3
# 5부터 시작. 앞에 아무것도 없으니 넘어감. 2 앞 숫자를 봄. 자기보다 작은 수가 없음. 넘어감. 7 앞 숫자를 봄. 자기보다 작은 수가 있으니 2개 다 지움. 
# 6 앞 숫자를 봄. 자기보다 작은 수가 없음. 넘어감. 8 앞 숫자를 봄. 6이 자기보다 작으니 지움. 7까지 지우려했더니 이미 3개 다 지웠음. 7 8 이렇게 남음.
# 이미 3개 다 지웠으니 나머지는 다 갖다 붙힘. 7 8 2 3 이됨

num , m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for x in num:
	while stack and m>0 and stack[-1]<x:
		stack.pop()
		m-=1
	stack.append(x)

if m != 0:
	stack=stack[:-m]

res = ''.join(map(str, stack))
print(res)