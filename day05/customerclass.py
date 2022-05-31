import json,re,sys

class Customer:
    custlist=[]

    def loadData(self):
        with open('./day02/customerdata.json','r') as f:
            self.custlist = json.load(f)

    def insertData(self):
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
            for i in self.custlist:
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
        self.custlist.append(customer)
        print(self.custlist)
        self.page = len(self.custlist)-1

    def curSearch(self):
        if self.page >= 0:
            print(f'현재 페이지는 {self.page+1}페이지 입니다.')
            print(self.custlist[self.page])
        else:
            print('입력된 데이터가 없습니다.')

    def preSearch(self):
            if self.page <= 0:
                print('첫번째 페이지 이거나 데이터가 없습니다.')
                print(self.page)
            else:
                self.page -= 1
                print(f'현재 페이지는 {self.page+1}페이지 입니다.')
                print(self.custlist[self.page])

    def nextSearch(self):
        if self.page >= len(self.custlist)-1:
            print('마지막 페이지 입니다.')
        else:
            self.page +=1
            print(f'현재 페이지는 {self.page+1}페이지 입니다.')
            print(self.custlist[self.page])

    def updateData(self):
        while True:
            choice1=input('수정할 이메일 주소>>>')
            idx = -1
            for i in range(len(self.custlist)):
                if self.custlist[i]['email'] == choice1:
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
                self.custlist[idx][choice2]=input(f'수정할 {choice2}를 입력>>>')
            elif choice2 =='exit':
                print('수정 종료')
            else:
                print('존재하지 않는 항목')
            print(self.custlist)
            break

    def deleteData(self):
            input1=input('삭제하려는 이메일>>>')
            delok = 0
            for i in range(len(self.custlist)):
                if self.custlist[i]['email'] == input1:
                    print('{}고객님의 정보 삭제'.format(self.custlist[i]['name']))
                    del self.custlist[i]
                    delok = 1
                    break
            if delok == 0:
                print('등록되지 않은 이메일')
            print(self.custlist)
            
    def saveData(custlist):
        with open('./day02/customerdata.json','w') as f:
            json.dump(custlist,f,indent=True)

    def exe(self,choice):
        if choice=='I':
            self.insertData() #주소가 넘어오니 리턴 안해줘도 되는데 숫자나 문자는 리턴처리 필수
        elif choice=='C':
            self.curSearch()
        elif choice=='P':
            self.preSearch()
        elif choice=='N':
            self.nextSearch()
        elif choice=='U':
            self.updateData()  
        elif choice=='D':
            self.deleteData()
            self.page=len(self.custlist)-1 #마지막 값이면 -1
        elif choice=='Q':
            self.saveData()
            print('저장 후 종료함')
            sys.exit()
                
    def display(self): #값만 넘겨주면 되니깐 리턴
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
        return choice

    def __init__(self): #개체생성되면 초기화
        self.loadData()
        self.page=len(self.custlist)-1
        while True:
            self.exe(self.display())

Customer()