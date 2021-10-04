flag = 1
while( flag ):
    try:
        r,w,l=map(int,input().split(' '))
        
        if(r == 0):
            flag=0
            break
        
    
        if(4*r**2>=w**2+l**2):
            print('Pizza {0} fits on the table.'.format(flag))
        else:
            print('Pizza {0} does not fit on the table.'.format(flag))
        flag+=1
    except:
        print('error')
    