n=list(input().split(' '))
if n[0]=='S' and n[1]=='P':
    print("Vignesh")
elif n[0]=='S' and n[1]=='R':
    print("Charan")
elif n[0]=='P' and n[1]=='S':
    print("Charan")
elif n[0]=='P' and n[1]=='R':
    print("Vignesh")
elif n[0]=='R' and n[1]=='P':
    print("Charan")
elif n[0]=='R' and n[1]=='S':
    print("Vignesh")
else:
    print("NULL")
