class FindAverage(object):
    def __init__(self, korean, english, math):
        self.__korean = korean
        self.__english = english
        self.__math = math

    @property
    def korean(self):    # getter
        return self.__korean

    @property
    def english(self):
        return self.__english

    @property
    def math(self):
        return self.__math

    def AddThree(self):
        return self.__korean + self.__english + self.__math


list1 = list(map(int, input().split(',')))  # 정수형 변수 3개 입력 받는 예제
student = FindAverage(list1[0], list1[1], list1[2])

print('국어, 영어, 수학의 총점:', FindAverage.AddThree())
