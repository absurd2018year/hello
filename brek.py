cc_1 = int(input())
count=1
temp = cc_1
for x in range(1,6):
	temp=temp//10 
	if temp>=1:
		count += 1
print(count)	