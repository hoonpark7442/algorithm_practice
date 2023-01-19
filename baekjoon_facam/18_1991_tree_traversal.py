# https://www.acmicpc.net/problem/1991
# 07. 고급 탐색 알고리즘 - 기초 문제풀이
# 문제유형: 트리, 구현

# 문제풀이 핵심 아이디어
# - 전위 순회: 루트 -> 왼쪽 자식 -> 오른쪽 자식
# - 중위 순회: 왼쪽 자식 -> 루트 -> 오른쪽 자식
# - 후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 루트

# - 트리는 보통 재귀로 구현
# - 중위 순회 특징은 x축 기준 왼쪽부터 오른쪽으로 쭉 출력되는 것을 알 수 있다(05:25 참고)

# - 트리 자료구조는 보통 데이터 개수 적을 땐 딕셔너리로 구현

class Node:
	def __init__(self, data, left_node, right_node):
		self.data = data
		self.left_node = left_node
		self.right_node = right_node


def pre_order(node):
	print(node.data, end='')
	if node.left_node != '.':
		pre_order(tree[node.left_node])
	if node.right_node != '.':
		pre_order(tree[node.right_node])

def in_order(node):
	if node.left_node != '.':
		in_order(tree[node.left_node])
	print(node.data, end='')
	if node.right_node != '.':
		in_order(tree[node.right_node])

def post_order(node):
	if node.left_node != '.':
		post_order(tree[node.left_node])
	if node.right_node != '.':
		post_order(tree[node.right_node])
	print(node.data, end='')

n = int(input())
tree = {}
for i in range(n):
	data, left_node, right_node = input().split()
	tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])




