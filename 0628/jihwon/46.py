class Student: #parent class
    name=''
    
class GraduateStudent(Student):
    major=''
    
a=Student()
a.name='홍길동'
b=GraduateStudent()
b.name='이순신'
b.major='컴퓨터'

print('이름:',a.name)
print('이름: {0}, 전공: {1}'.format(b.name, b.major))