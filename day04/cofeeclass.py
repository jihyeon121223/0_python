import json,sys

class  coffee:
    coffee={'아메리카노':3000}

    def data_load(self,path): 
        f = open(path,'r') #밑에꺼 먼저 하고 나중에 주석풀어서 읽기
        self.coffee=json.load(f) 
        f.close()

    def data_input(self):
        item=input('메뉴>>>')
        price=int(input('가격>>>'))
        self.coffee[item]=price
        print(coffee)

    def data_delete(self):
        print(coffee.keys())
        item = input('삭제할 메뉴명>>>')
        del self.coffee[item]
        print(coffee)

    def data_update(self):
        print(coffee.keys())
        item=input('메뉴>>>')
        price=int(input('가격>>>'))
        self.coffee[item]=price
        print(coffee)

    def data_list(self): #변경되지않기때문에 리턴안해줘
        for k,v in self.coffee.items(): #self입력 안해줘서 리스트가 안떳음
            print(f'{k:^10} {v:,}')

    def data_save(self):
        f = open('./day04/coffee.data','w') 
        json.dump(self.coffee,f)
        f.close()


    def exe(self):
        display = '''
    -----------------
    1.메뉴입력 2.메뉴삭제 3.메뉴수정 4.메뉴리스트 5.종료
    -----------------
    >>> '''
        menu=input(display)
        if menu=='5': 
            print('프로그램종료')
            self.data_save()
            sys.exit()
        elif menu=='1':
            self.data_input()
        elif menu=='2':
            self.data_delete()
        elif menu=='3':
            self.data_update()
        elif menu=='4':
            self.data_list()

    def __init__(self):
        self.data_load('./day04/coffee.data')
        while True:
            self.exe()

coffee()