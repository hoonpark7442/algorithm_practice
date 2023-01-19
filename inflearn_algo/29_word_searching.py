# 섹션5. 자료구조 활용(스택,큐,해쉬,힙)
# 8. 단어 찾기(해쉬)

# 걍 드는 생각은...단어를 키로 밸류를 일단 0으로 초기화하고.. n-1 단어 나올때 그 단어의 밸류를 1로 업뎃하고.. 나중에 밸류가 0인 애를 출력...그런데 밸류로 찾으면 해시쓰는 이유가 없지 않아..?

# 대충 맞네... 설명은 초기에 1로 세팅하고 그 단어 쓰이면 1을 깎는 식으로..

n=int(input())
p=dict()
for i in range(n):
	word = input()
	p[word]=1

for i in range(n-1):
	word=input()
	p[word]=0

for key, val in p.items():
	if val==1:
		print(key)
		break