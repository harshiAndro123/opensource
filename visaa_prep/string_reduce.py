s=input()
r=[]
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        r.append(s[i-1]+str(count))
        count=1
r.append(s[i]+str(count))
print(''.join(r))
