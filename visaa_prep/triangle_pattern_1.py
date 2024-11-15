n=int(input())
n_i=1
for i in range(n):
    for j in range(i+1):
        print(n_i,end=' ')
        n_i+=1
    print()
