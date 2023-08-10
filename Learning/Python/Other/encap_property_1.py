class Score():
    def __init__(self, score):
        self.__score = score

    @property
    def sc(self):
        print('inside the getscore')
        return self.__score
    
    @sc.setter
    def sc(self, score):
        print('Inside the setscore')
        self.__score = score

stu = Score(0)
print(stu.sc)
print('*' * 20)
stu.sc = 80
print(stu.sc)