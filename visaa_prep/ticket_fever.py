t=int(input())
for i in range(t):
    a=list(map(int,input().split(' ')))
    if a[0]>a[1]:
        d=a[0]-a[1]
        print(d)
    else:
        print("0")
