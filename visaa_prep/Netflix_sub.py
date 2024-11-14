n=list(map(int,input().split(' ')))
if n[0]+n[1]>=n[3] or n[1]+n[2]>=n[3] or n[0]+n[2]>=n[3]:
    print("YES")
else:
    print("NO")
