# https://www.acmicpc.net/problem/1543
# 05. 기본 탐색 알고리즘 - 기초 문제풀이

# 어떻게 풀어야 할까 - 내 생각
# 문서줄에서 검색어(연속된 캐릭터) 있으면 문서줄에서 지우고 카운트 올림
# 다시 편집된 문서줄 돌려서 또 검색어 찾음. 있으면 카운트 올림

# docs = input()
# search = input()
# count = 0
# for i, char in enumerate(search, start=0):
# 	if char == docs[i]

# 일단 시간초과로 여기서 멈춤... 대충 아이디어는 검색어 렝쓰만큼 돌면서 연속된 캐릭터가 닥스에 있는지 보고 있으면 카운트 올리고 닥스에서 해당 문자열 뺌


# 핵심 아이디어
# - 문서 길이는 최대 2,500이고 단어 길이는 최대 50
# - 단순히 모든 경우의 수 계산하여 문제 해결 가능
# - 시간복잡도 O(NM)의 알고리즘으로 해결 가능


# 문제풀이

document = input()
word = input()

index = 0
result = 0

while len(document) - index >= len(word):
	if document[index:index + len(word)] == word: # 인덱스부터:단어의 길이 만큼. 그게 이제 단어랑 같으면
		result += 1
		index += len(word)
	else:
		index += 1

print(result)
