import sys
#sys.stdin=open("input.txt","rt")

n=int(input())

pp=[]
for i in range(n):
    a,b=map(int,input().split())
    pp.append((a,b))

pp.sort(reverse=True)
cnt=1
(resH,resW)=pp[0]

for i in range(1,n):
    tempH,tempW=pp[i]
    if tempH<=resH and tempW<=resW:
        continue
    else:
        cnt+=1
        resH,resW=pp[i]
print(cnt)
