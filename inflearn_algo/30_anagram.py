# 섹션5. 자료구조 활용(스택,큐,해쉬,힙)
# 9. 애너그램(딕셔너리 해쉬)

# 흠...그냥 두 문자열 다 해시로 만들고.. 해시구성은 키값은 단어, 밸류는 카운트 이렇게 해서.. 다른 문자열 해쉬랑 비교..?
# 아니면 밸류를 서로 빼는 식으로..? 만약 밸류가 0이 아니라면 그건 아나그램 아니니 'no' 출력?

# a=input()
# b=input()
# str1=dict()
# str2=dict()

# for x in a:
# 	str1[x] = str1.get(x, 0) + 1

# for x in b:
# 	str2[x] = str2.get(x, 0) + 1	

# for i in str1.keys():
# 	if i in str2.keys():
# 		if str1[i] != str2[i]:
# 			print("NO")
# 			break
# 	else:
# 		print("NO")
# 		break

# # for i in str2.keys(): -> 요건 필요가 없는게 문제 조건에 길이가 일치해야 된다고 되어있다..
# # 	if i not in str1.keys():
# # 		print("NO")
# # 		break

# else:
# 	print("YES")

# 개선된코드

a=input()
b=input()
str=dict()

for x in a:
	str[x] = str.get(x, 0) + 1

for x in b:
	str[x] = str.get(x, 0) - 1

for x in a:
	if str.get(x) > 0:
		print("NO")
		break

else:
	print("YES")