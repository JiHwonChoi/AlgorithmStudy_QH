from typing import List

def elecbus(power: int,fin: int ,howmany: int,charger :List[int]) -> int :
    count=0;
    while(fin>0):
        start=fin-power
        #출발점을 찾았을 경우
        if(start<=0):
            break
        
        #충전소있나 찾아보기
        for i in range(start,fin+1):
            
            #충전소 발견
            if i in charger:
                fin=i
                count+=1
                #충전소 중복 방지 위해 한번 이용한 충전소는 삭제
                charger.remove(i)
                break
            
            #충전소가 없을경우
            if (i == fin):
                return 0
        
    
    return count        

#거꾸로 가면서 풀어보기
busline = int(input())
ans=[]
for i in range(busline):
    num=list(map(int,input().split(' ')))
    K=num[0]
    N=num[1]
    M=num[2]
    charger=list(map(int,input().split(' ')))
    ans.append(elecbus(K,N,M,charger))

for i,value in enumerate(ans):
    k=i+1
    print(f'#{k} {value}')