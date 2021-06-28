class Shape:
    
    def area() :
        return 0

    
class Square(Shape):
    
    length=3
    
    def area(self):
        return (int(self.length)*int(self.length))
    
a=Square()

print('정사각형의 면적: {0}'.format(a.area()))