class Student:
    
    scoreTot=0
    
    def setScore(self, KOR, ENG, MATH):
        self.KOR=int(KOR)
        self.ENG=int(ENG)
        self.MATH=int(MATH)
        
        scoreTot=self.MATH+self.KOR+self.ENG
        print('국어, 영어, 수학의 총점:', scoreTot)
        
    def __init__(self) -> None:
        KOR, ENG, MATH = input().split(',')
        self.setScore(KOR,ENG,MATH)
        
        
a = Student()

