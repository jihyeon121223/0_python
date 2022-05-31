# 콘솔형 고객 정보 관리 시스템 구축

# 1. 기능  
# 고객 정보 입력(I), 현재/이전/다음 고객 정보 조회(C/P/N), 고객 정보 수정(U), 고객 정보 삭제(D), 고객 정보 종료(Q)

# - 괄호 안 영문자를 입력하면 각 기능이 구현되게 만든다
# - 종료(Q)를 입력하기 전까지 기능 선택 메시지가 계속 뜨도록 만든다
# - 입력된 각 정보는 인덱스 값에 따라 페이지를 가진다
#   -> 첫 정보 입력 시 인덱스는 0이므로, 입력 전 기본 page 값은 -1로 설정한다

# 2. 입력(I)
# - dictionary로 각 키의 값을 받고 빈 리스트에 채워나간다 
# - 성별(gender) : M, m, F, f로만 입력 가능 
#   -> 소문자로 입력하는 경우 대문자로 자동 변환 
#   -> gender 값이 M 또는 F가 아닐 경우 다시 입력 
# - 이메일(email) : 입력값 내 '@'가 반드시 있어야 함 '''
#   -> 정규표현식 사용
#   -> re를 import 하여 이메일 입력값 내 '@' 존재 여부 파악 
#   -> 없는 경우 '@'를 포함하라는 문구와 함께 재입력 하도록 함 
# - 출생년도(birthyear) : 4자리로 입력 해야 
#   -> len 값으로 입력 값의 길이를 구함 
#   -> 4자리가 아닐 경우 재입력 하도록 함 
# - 출생년도까지 입력이 완료되었을 경우
#   -> 키 값 입력이 완료된 customer 딕셔너리를 custlist 리스트에 추가(append)한다
#   -> 고객 정보가 새로 입력 되었으므로 page 값에 1을 더한다

# 3. 조회(C, P, N)
# - 인덱스는 0부터 시작하나 페이지는 통상 1부터 시작하므로 페이지 출력시 page+1 값을 반환한다
# - 이전 페이지 조회(P)의 경우, 첫 번 째 페이지인 상태에서 이전 페이지로 이동이 불가하므로 현재 페이지인 첫 번 째 페이지를 반환
# - 다음 페이지 조회(N)의 경우, 마지막 페이지인 상태에서 다음 페이지로 이동이 불가하므로 현재 페이지인 마지막 페이지를 반환

# 4. 삭제(D)
# - unique한 키를 기준으로 삭제정보를 선택한다 -> 여기서는 이메일로 가정
# - 삭제 성공 여부 변수(delok)
#   -> 입력한 이메일이 등록된 정보 내에 있을 경우 삭제
#   -> 삭제가 성공하면 delok=1 (default 값 0)
#   -> 등록된 정보 내에 없는 이메일일 경우(delok=0) 등록되지 않았다고 출력

# 5. 수정(U)
# - unique한 키를 기준으로 수정 정보를 선택한다 -> 여기서는 이메일로 가정
# - 입력한 이메일과 일치하는 고객 정보의 인덱스를 idx에 입력
#   -> idx의 default 값은 -1
#   -> 일치 여부 확인 후에도 idx가 -1일 경우 등록되지 않았다고 출력
# - 이메일 외에 이름, 성별, 출생년도 중 수정할 정보 선택
# - 수정할 정보 선택 후 수정할 내용 입력
# - 수정하고 픈 변수가 없는 경우 exit 입력 시 수정 창 종료

# 6. 종료(Q)
# - 맨 처음 while 반복문을 나간다 -> break


import re

from soupsieve import select
custlist=[{'name': 'ddd', 'gender': 'f', 'email': 'yjh12@naver.com', 'birthyear': '2000'}
        ,{'name': 'sss', 'gender': 'f', 'email': 'yjt12@naver.com', 'birthyear': '2002'}
        ,{'name': 'aaa', 'gender': 'f', 'email': 'yjr12@naver.com', 'birthyear': '2003'}
        ,{'name': 'eee', 'gender': 'f', 'email': 'yje12@naver.com', 'birthyear': '2004'}
        ]
page=3
 
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

    if choice=="I":  
        customer={'name':'','gender':'','email':'','birthyear':''}
        customer['name']=input('이름입력>>>')
        while True:
            customer['gender']=input('성별(M/F)입력>>')
            if customer['gender'].upper() in ('M','F'):
                break

        while True:
            p=re.compile('[a-zA-Z][a-z0-9]{4,}@[a-z]{2,}[.][a-z]{2,}')
            while True:
                customer['email']=input('이메일입력>>>')
                pcheck=p.match(customer['email'])
                if pcheck:
                    break
                else:
                    print('이메일 형식을 확인해주세요')
            check=0
            for i in custlist:
                if i['email']==customer['email']:
                    check=1
                    break
            if check ==0:
                break
            print('중복되는 이메일이 있습니다')
        
        while True:
            customer['birthyear']=input('출생년도 4자리 입력>>>')
            if len(customer['birthyear'])==4 and customer['birthyear'].isdigit():
                break
        custlist.append(customer)
        print(custlist)
        page=len(custlist)-1

        pass

    elif choice=="C": 
        if page >= 0:
            print('현재 페이지는 {page+1}페이지입니다')
            print(custlist[page])
        else:
            print('입력데이터없음')
    elif choice == 'P':
        if page <= 0:
            print('첫페이지이거나 데이터없음')
            print(page)
        else:
            page -= 1
            print('현재 페이지는 {page+1}페이지입니다')
            print(custlist[page])
    elif choice == 'N':
        if page >= len(custlist)-1:
            print('마지막페이지입니다')
        else:
            page += 1
            print('현재 페이지는 {page+1}페이지입니다')
            print(custlist[page])
    elif choice=='D':
        while True:
            delok=0
            p=re.compile('[a-zA-Z][a-z0-9]{4,}@[a-z]{2,}[.][a-z]{2,}')
            while True:
                pcheck=p.match(customer['email'])
                if pcheck:
                    del pcheck
                    delok=1
                    break
                else:
                    print('등록된 이메일이 아닙니다')
    elif choice=="U": 
        while True:
            p=re.compile('[a-zA-Z][a-z0-9]{4,}@[a-z]{2,}[.][a-z]{2,}')
            idx=0
            while True:
                pcheck=p.match(customer['email'])
                if i['email']==customer['email']:
                    break
                elif idx ==-1:
                    break
                print('등록된 정보가 없습니다')
                if i['name']==customer['name']:
                    break
                elif idx ==-1:
                    break
                print('등록된 정보가 없습니다')
                if i['gender']==customer['gender']:
                    break
                elif idx ==-1:
                    break
                print('등록된 정보가 없습니다')
                if i['birthyear']==customer['birthyear']:
                    break
                elif idx ==-1:
                    break
                print('등록된 정보가 없습니다')
            if input('수정종료는 exit입력>>')
                break
                        
    elif choice=="Q":
        def data_save(custlist):
        f = open('','w') 
        json.dump(custlist,f)
        f.close()
        break