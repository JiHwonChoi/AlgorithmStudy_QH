class subject :
    def __init__(self,kor,eng,math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math


score = input().split(',')
student = subject(int(score[0]),int(score[1]),int(score[2]))

print("국어, 영어, 수학의 총점: {}".format(student.total()))
        
