# https://www.acmicpc.net/problem/2747
# 03. 재귀호출 - 핵심유형 문제풀이


# 아래와 같이 재귀함수로 풀면 시간 초과된다. 동적프로그래밍으로 풀던가 반복문으로 풀어야 함
# def fibo(n):
# 	if n == 0:
# 		return 0
# 	if n == 1:
# 		return 1
# 	return fibo(n-1) + fibo(n-2)

# print(fibo(int(input())))


# 반복문으로 푸는 법
# n = int(input())

# a, b = 0, 1

# while n > 0:
# 	a, b = b, a+b
# 	n -= 1

# print(a)

# dp로 푸는 법
def fibo(n):
	n += 1
	cache = [0]*n

	cache[1] = 1

	for i in range(2, n):
		cache[i] = cache[i-1] + cache[i-2]

	return cache[-1]

n = int(input())

print(fibo(n))