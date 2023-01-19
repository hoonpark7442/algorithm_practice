# 섹션5. 자료구조 활용(스택,큐,해쉬,힙)
# 9.1. 애너그램(리스트 해쉬)

# 리스트를 해시처럼 사용해서 푸는 방법. 아스키코드 사용한다.
# 알파벳 대문자의 아스키코드는 65~90 이다. 총 26개.
# 알파벳 소문자의 아스키코드는 97~122 이다. 총 26개.

# 그러니 리스트를 처음 초기화할 때 str1=[0]*52 이렇게 할건데, 대문자A는 0번째 들어와야 되니 대문자일 경우 -65를 해주고
# 소문자a는 26번째부터 들어가야 되니 97에서 71을 빼준다.

a=input()
b=input()
str1=[0]*52
str2=[0]*52

for x in a:
	if x.isupper():
		str1[ord(x)-65]+=1
	else:
		str1[ord(x)-71]+=1

for x in b:
	if x.isupper():
		str2[ord(x)-65]+=1
	else:
		str2[ord(x)-71]+=1

for i in range(52):
	if str1[i] != str2[i]:
		print("NO")
		break

else:
	print("YES")