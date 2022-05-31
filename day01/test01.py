# a=0o177 #8진수를 10진수로 바꾸면 127
# print(a) #표준출력
# print(type(a)) #127 <class 'int'>

# data=input('숫자를 입력하세요:>>>') #표준입력 
# print(data)
# print(type(data)) #123<class 'str'> 안에 든 데이터 유형을 보여줌: 숫자인지, 문자인지 

# #ctrl+/ 하면 전체 주석 처리됨

# #들어오는게 문자인데 숫자로 계산하려면 
# data=input('숫자를 입력하세요:>>>')
# data=int(data) #숫자로 바꾸기
# print(data)
# print(type(data))

# #박스당 들어가는 과일, 몇개 남는지 출력
# data=input("박스:") #int써야지 정수 계산 가능
# data=input("개:")
# print(data)
# 나누기, 몫 연산자 사용
# data1=int(input("박스당 과일 수:"))
# data2=int(input("과일 수:"))
# print(data2//data1, '박스', data2%data1, '남음')


# """as 
# sd""" #중간 엔터쓴채로 출력 가능
# "asd'sd"
# '"asd"' #안에 있는 모든걸 문자로 취급(그러나 따옴표/작은따옴표 다르게 써야함. 'asd'sd' 처럼 같은거 쓰면 문자 취급 안함)

# a="""as 
# sd"""
# b="asd'sd"
# print(a)
# print(b)


# print('Python'+' is fun!') # 문자열 사이에서 +는 연결. 스페이스 해야 안 붙음 
# # print('python '+2) #에러. 같은 문자나 숫자끼리만 연결 가능. 
# print('python'*2) #*는 반복.

# print(len('life is too')) #문자열길이(공백포함)


a = "Life is too short"
print(a[3]) #e   인덱스값은 0부터 시작하고 []안에 있다. 
print(a[-3]) #o  뒤로 셈. 지칭은 대괄호 [].