# 섹션5. 자료구조 활용(스택,큐,해쉬,힙)
# 4. 후위연산(스택)

# 흠...숫자아닌거 나오면 바로 뒤랑 그 뒤, 즉 a[-1], a[-2]를 그 연산자를...어케 적용하지..?여튼 적용해서 계산. 
# 아니면 숫자는 스택에 넣어. 숫자 아닌거 나오면 맨 위 2개 팝해. 연산자 적용해서 다시 스택에 넣어. 이런식으로.
# 352+*9-
# 3,5,2를 스택에 넣는다. + 만났으니 맨 위 2개, 즉 2와 5를 꺼낸다...근데 2+5가 아니가 5+2가 되어야 할거같은데...
# 여튼 더해서 7을 다시 스택에 넣는다. 그럼 스택에는 3, 7이 들어가있다. * 만났다. 다시 꺼낸다. 7,3 순으로 꺼내겠지만 계산은 3*7 을 한다. 
# 21을 스택에 넣는다. 9를 스택에 넣는다. - 만났다. 그럼 9, 21 을 꺼낸다. 꺼낸 숫자 반대로 21-9를 한다. 

# 문제풀이
# 일단 내 생각이 맞다.

a=input()
stack = []
for x in a:
	if x.isdecimal():
		stack.append(int(x))
	else:
		if x=='+':
			n1=stack.pop()
			n2=stack.pop()
			stack.append(n2+n1)
		elif x=='-':
			n1=stack.pop()
			n2=stack.pop()
			stack.append(n2-n1)
		elif x=='*':
			n1=stack.pop()
			n2=stack.pop()
			stack.append(n2*n1)
		elif x=='/':
			n1=stack.pop()
			n2=stack.pop()
			stack.append(n2/n1)

print(stack[0])