a=int(input())
for i in range(a):
    N,M=map(int,input().split(' '))
    num=list(map(int, input().split(' ')))
    listSum=[]
    
    for j in range(len(num)-(M-1)):
        Msum=0
        for k in range(M):
            Msum+=num[j+k]
        listSum.append(Msum)
    print(max(listSum)-min(listSum))