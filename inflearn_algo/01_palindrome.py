# n=int(input())
# for i in range(n):
# 	s=input()
# 	s=s.upper()
# 	size=len(s)
# 	for j in range(size//2):
# 		if s[j]!=s[-1-j]:
# 			print("#%d NO" %(i+1))
# 			break
# 	else:
# 		print("#%d YES" %(i+1))


# n=int(input())
# for i in range(n):
# 	s=input()
# 	s=s.upper()
# 	if s==s[::-1]:
# 		print("Yes")
# 	else:
# 		print("No")





# n = int(input())

# for _ in range(n):
# 	s = input().upper()
# 	if s == s[::-1]:
# 		print("Yes")
# 	else:
# 		print("no")
# a




n = int(input())

for _ in range(n):
	s = input().upper()
	size = len(s)
	for j in range(size//2):
		if s[j] != s[-1-j]:
			print("NO")
			break
	else:
		print("YES")
		







