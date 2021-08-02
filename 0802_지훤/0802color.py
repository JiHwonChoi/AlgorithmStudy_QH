# 2 2 4 4 1
a= int(input())
for i in range(a):
    
    color1=[]
    color2=[]
    count=0
    
    b= int(input())
    
    for j in range(b):
        info=[]
        info=list(map(int,input().split(' '))) #start_x, start_y, end_x, end_y, color
        
        if (info[4] == 1):
            color=color1
        else:
            color=color2
            
        for x in range(info[0],info[2]+1):
            for y in range (info[1], info[3]+1):
                color.append((x,y))
        
    print (color1)
    print (color2)
    for xy in color1:
        if(xy in color2):
            count+=1
    print(count)