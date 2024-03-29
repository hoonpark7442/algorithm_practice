# https://www.acmicpc.net/problem/1904
# 09. 동적 프로그래밍 - 01. 기초 문제풀이
# 문제유형: 동적프로그래밍

# 문제풀이 핵심 아이디어
# - 사용할 수 있는 타일 종류는 2개
# - 두가지 종류의 타일을 이용하여 N 길이의 수열을 만드는 모든 경우의 수를 구해야 한다
# - 가장 전형적인 동적 프로그래밍 문제
# - N이 최대 1백만이므로 시간복잡도 O(N)으로 해결해야 함

# - 동적프로그래밍은 한 번 계산한 값은 다시 계산하지 않는다. 메모이제이션
# - 동적 프로그래밍 문제를 풀기 위해서는 점화식(인접한 항들 사이의 관계식)을 세워야 한다.
# - D[i] = '수열의 길이가 i 일 때의 경우의 수'라고 하자
# - 예를 들어 D[3] = 3, D[4] = 5 이다.

# 타일을 왼쪽에서부터 오른쪽으로 이어서 붙인다고 가정하자
# 생각해보면 길이가 i인 수열을 형성하는 방법은 다음의 두가지 뿐이다.

# i-1 까지의 조합의 마지막에 1을 붙이는 경우
# i-2 까지의 조합의 마지막에 00을 붙이는 경우
# 따라서 D[i] = '수열의 길이가 i일 때의 경우의 수'라고 하면
# D[i] = D[i-1] + D[i-2]
# 다시말해 이 문제는 피보나치 수열과 동일한 문제이다.

n = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
	dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])
