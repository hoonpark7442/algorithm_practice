# 섹션5. 자료구조 활용(스택,큐,해쉬,힙)
# 3. 후위표기식 만들기(스택)

# 이것도 손도 못대겠는데...
# 3+5*2/(7-2)
# 곱하기나 나누기면 뒤에숫자 붙인 후 바로 뺀다. 
# 괄호여도 닫는 괄호 뒤에 바로 뺀다.
# 3 리스트 넣고, +는 스택에 넣고 5는 리스트 붙이고, *니까 뒤에꺼 리스트 붙이자마자 바로 스택 팝해서 붙여. 이렇게하면 일단 352* 까지 됨
# 나누기니까 또 뒤어꺼 리스트로 붙이고 바로 스택팝할건데, 괄호가 나왔으니 일단 7과 2 붙이고 닫는괄호 만났으니 - 붙여. 이렇게 하면 352*72- 까지 됨
# 나누기 바로 팝해서 붙여. 352*72-/ 이거임. 이제 스택에 남은거 다 팝해서 붙여. 352*72-/+

# 문제풀이
# 흠...그니까 * 나 / 만나면 스택 상단에서 자기랑 우선순위 같거나 빠른게 있으면 빼낸다. 없으면 걍 스택에 집어넣고..
# 이건 코드 설명 봐도 좀 어렵다..

a=input()
stack=[]
res=''

for x in a:
	if x.isdecimal():
		res+=x
	else:
		if x=='(':
			stack.append(x)
		elif x=='*' or x=='/':
			while stack and (stack[-1]=='x' or stack[-1]=='/'):
				res+=stack.pop()
			stack.append(x)
		elif x=='+' or x=='-':
			while stack and stack[-1]!='(':
				res+=stack.pop()
			stack.append(x)
		elif x==')':
			while stack and stack[-1]!='(':
				res+=stack.pop()
			stack.pop()

while stack:
	res+=stack.pop()

print(res)