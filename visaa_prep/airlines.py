n=list(map(int,input().split(' ')))
tot=n[0]*100
if tot>=n[1]:
    need=0
else:
    need=(n[1]-tot+99)//100
print(need)
