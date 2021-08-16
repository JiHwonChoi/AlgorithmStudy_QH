arr=[1,2,3,4,5,6,7,8,9,10,11,12]
n=len(arr)
subset=[]

for i in range(1<<n):
    sublist=[]
    for j in range(n):
        if i&(1<<j):
            sublist.append(arr[j])
    subset.append(sublist)
cnt=0
#이건 푼게 아니야ㅜㅜ

a,b=map(int,input().split(' '))
for i in subset:
    if((len(i)==a)and(sum(i)==b)):
        cnt+=1
print(cnt)
            