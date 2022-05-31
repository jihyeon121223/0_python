class calculator: #상속없으면 :, 있으면 ()
    def __init__(self):
        self.result=0 #만들면서 동작시킬때 변수명을 그냥안쓰고 셀프붙임. 따로 선언안해도됨

    def add(self,num):
            self.result += num
            return self.result 

    def setdata(self,first,second):
        self.first=first
        self.second=second #=매게변수. 를 앞=에 넣어준다

# cal1 = calculator()
# cal2 = calculator()
# print(cal1.result)
# print(cal2.result)
# print(cal1.add(5))
# print(cal1.add(3))
# print(cal2.result)

a=calculator()
print(type(a))
a.setdata(4,2)