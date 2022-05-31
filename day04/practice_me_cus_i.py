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


import re
custlist=[]
page=-1
 
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
        info=['name','gender','email','birthyear']
        name=input('name:')
        gender=input('gender:')
        email=input('email:')
        birthyear=input('birthyear:')
        
        if gender.upper[2]=='m' or gender.upper[2]=='f':
            pass
        else:    
            print('m 또는 f로 다시 입력해주세요')
            
        if email[3]== re.compile('[a-zA-Z][a-z0-9]{4,}@[a-z]{2,}[.][a-z]{2,}'):
            pass
        else:
            print('@를 포함하여 다시 입력해주세요')
            
        if birthyear[4]==int(len(3)):
            pass
        else:
            print('년도 4자리를 다시 입력해주세요')
        
        custlist.append


        pass
    elif choice=="C": 
        pass
    elif choice == 'P':
        pass
    elif choice == 'N':
        pass
    elif choice=='D':
        pass
    elif choice=="U": 
        pass
    elif choice=="Q":
        break


