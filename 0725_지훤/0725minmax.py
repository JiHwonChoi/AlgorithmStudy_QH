a= int(input())
ans=[]
for i in range(a):
    b= int(input())
    minmax = list(map(int,input()))
    minmax.sort()
    ans.append(minmax[-1]-minmax[0])
for i,value in enumerate(ans):
    k=i+1
    print(f'#{k} {value}')
       