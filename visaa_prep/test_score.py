n=list(map(int,input().split(' ')))
if n[2]%n[1]==0 and n[2]//n[1]<=n[0]:
    print("YES")
else:
    print("NO")
