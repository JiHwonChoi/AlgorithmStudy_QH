
#세로N 가로M
n,m=map(int,input().split(' '))

floor=list()
cnt=0

for i in range(n):
    floor.append(input())

#세로로 탐색
for i in range(m):
    for j in range(n):
        if(floor[j][i]=='|'):
            if (j<=n-2 and floor[j+1][i]=='-'):
                cnt+=1
            elif(j==n-1):
                cnt+=1
           



#가로로 탐색
for j in range(n):
    for i in range(m):
        # print(floor[j][i], j,i)
        if(floor[j][i]=='-'):
            if(i<=m-2 and floor[j][i+1]=='|'):
                cnt+=1
            elif(i==m-1):
                cnt+=1
print(cnt)


# a='---||--|-' #9개
# cnt=0
# print(a)
# for i,v in enumerate(a):
#     if(v =='-' and i < len(a)-1):
#         #-|
#         if(a[i+1]=='|'):
#             cnt+=1
#     elif(i==len(a)-1 and v=='-'):
#         cnt+=1
        
#     print('i:{0} cnt:{1}'.format(i,cnt))