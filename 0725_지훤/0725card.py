a=int(input())
for i in range(a):
    b=int(input())
    card=input()
    howmany=[0]*10
    # 0 0 0 0 0 0 0 0 0 6 
    for k in card :
        k=int(k)
        howmany[k]+=1
        
    #가장많은 카드의 숫자와 장 수
    maxNum=max(howmany)
    for j in range(10):
        if(howmany[j]>=maxNum):
            maxIndex=j
    times=i+1
    print(f'#{times} {maxIndex} {maxNum}')

    
        