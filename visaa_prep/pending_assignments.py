n=list(map(int,input().split(' ')))
m=n[0]*n[1]
y=n[2]*24*60
if y>=m:
    print("YES")
else:
    print("NO")
