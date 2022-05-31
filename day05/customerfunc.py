import json,re

def loadData():
    with open('./day05/customerdata.json','r') as f:
        custlist = json.load(f)
    return custlist

def insertData(custlist):
        customer={'name':'','gender':'','email':'','birthyear':''}
        customer['name'] = input('이름을 입력하세요 >>>')
        while True:
            customer['gender'] = input('성별(M/F)를 입력하세요 >>>')
            if customer['gender'].upper() in ('M','F'):
                break

        while True:
            p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}[.][a-z]{2,}')
            while True:
                customer['email']=input('이메일을 입력하세요 >>>')
                pcheck = p.match(customer['email'])
                if pcheck:
                    break
                else:
                    print('이메일을 형식에 맞춰 입력하세요')
            check = 0
            for i in custlist:
                if i['email']==customer['email']:
                    check = 1
                    break
            if check == 0:
                break
            print('중복되는 이메일이 있습니다.')
        
        while True:
            customer['birthyear']=input('출생년도 4자리로 입력해주세요 >>>')
            if len(customer['birthyear'])==4 and customer['birthyear'].isdigit():
                break
        custlist.append(customer)
        print(custlist)
        page = len(custlist)-1

def curSearch(custlist,page):
    if page >= 0:
        print(f'현재 페이지는 {page+1}페이지 입니다.')
        print(custlist[page])
    else:
        print('입력된 데이터가 없습니다.')

def preSearch(custlist,page):
        if page <= 0:
            print('첫번째 페이지 이거나 데이터가 없습니다.')
            print(page)
        else:
            page -= 1
            print(f'현재 페이지는 {page+1}페이지 입니다.')
            print(custlist[page])
        return page

def nextSearch(custlist,page):
    if page >= len(custlist)-1:
        print('마지막 페이지 입니다.')
    else:
        page +=1
        print(f'현재 페이지는 {page+1}페이지 입니다.')
        print(custlist[page])
    return page

def updateData(custlist):
       while True:
            choice1=input('수정할 이메일 주소>>>')
            idx = -1
            for i in range(len(custlist)):
                if custlist[i]['email'] == choice1:
                    idx=i
                    break
            if idx == -1:
                print('등록되지 않은 이메일')
                break
            choice2=input('''
 다음중 수정할 정보를 택하시오
 (name, gender, birthyear)
 수정할 정보가 없으면 exit입력
            ''')
            if choice2 in ('name','gender', 'birthyear'):
                custlist[idx][choice2]=input(f'수정할 {choice2}를 입력>>>')
            elif choice2 =='exit':
                print('수정 종료')
            else:
                print('존재하지 않는 항목')
            print(custlist)
            break

def deleteData(custlist):
        input1=input('삭제하려는 이메일>>>')
        delok = 0
        for i in range(len(custlist)):
            if custlist[i]['email'] == input1:
                print('{}고객님의 정보 삭제'.format(custlist[i]['name']))
                del custlist[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 이메일')
        print(custlist)
        
def saveData(custlist):
    with open('./day05/customerdata.json','w') as f:
        json.dump(custlist,f,indent=True)
