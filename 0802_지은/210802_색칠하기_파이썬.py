test_case = int(input())

for t in range(1,test_case+1):
    N = int(input())
    red = []
    blue = []

    for n in range(N):
        x1,y1,x2,y2,color = map(int,input().split())
        for i in range(x1, x2+1):
            for j in range(y1,y2+1):
                if color == 1:
                    
