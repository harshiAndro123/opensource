n=int(input())
d=list(map(int,str(n)))
sum1=0
for i in range(len(d)):
    sum1+=d[i]
if sum1%2==0:
    print("Vignesh")
else:
    print("Charan")
