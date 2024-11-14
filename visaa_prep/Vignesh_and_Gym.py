n=list(map(int,input().split(' ')))
m=n[0]+n[1]
if n[2]>n[0]:
    if n[2]>=n[0]+n[1]:
        print("2")
    else:
        print("1")
else:
    print("0")
