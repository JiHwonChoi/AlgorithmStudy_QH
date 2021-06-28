class Rectangle:
    w=0
    h=0
    area=0
    
    def __init__(self) -> None:
        self.w=4
        self.d=5
        self.area=self.w*self.d
        print('사각형의 면적: {0}'.format(self.area))
        
nemo=Rectangle()