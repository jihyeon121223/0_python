import re, sys
import customerfunc as cf



custlist=[]
custlist= cf. loadData()
page=len(custlist)-1
#print(custlist)

def exe(choice, page):
    if choice=='I':
        cf. insertData(custlist) #주소가 넘어오니 리턴 안해줘도 되는데 숫자나 문자는 리턴처리 필수
        print(custlist)
    elif choice=='C':
        cf. curSearch(custlist,page)
    
    elif choice=='P':
       page= cf.preSearch(custlist,page)

    elif choice=='N':
        page= cf. nextSearch(custlist,page)

    elif choice=='U':
        cf. updateData(custlist)
    
    elif choice=='D':
        cf. deleteData(custlist)
        page=len(custlist)-1 #마지막 값이면 -1
    elif choice=='Q':
        cf. saveData(custlist)
        print('저장 후 종료함')
        sys.exit()
    return page
            
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()  
    page=exe(choice, page)