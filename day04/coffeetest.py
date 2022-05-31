##커피자판기 메뉴입력 프로그램
import json #파일을 왔다갔다 계속 쓸 때 씀

f = open('./day04/coffee.data','r') #밑에꺼 먼저 하고 나중에 주석풀어서 읽기
coffee=json.load(f) 
f.close()

# coffee={'아메리카노':3000} #읽어왔는데 커피 제 정의하면 오류나니깐

while True:
    display = '''
-----------------
1.메뉴입력 2.메뉴삭제 3.메뉴수정 4.메뉴리스트 5.종료
-----------------
>>> '''
    menu=input(display)
    if menu=='5': 
        print('프로그램종료')
        break
    elif menu=='1':
        item=input('메뉴>>>')
        price=int(input('가격>>>'))
        coffee[item]=price
        print(coffee)
    elif menu == '2':
        print(coffee.keys())
        item = input('삭제할 메뉴명>>>')
        del coffee[item]
        print(coffee)
    elif menu=='3':
        print(coffee.keys())
        item=input('메뉴>>>')
        price=int(input('가격>>>'))
        coffee[item]=price
        print(coffee)
    elif menu=='4':
        for k,v in coffee.items():
            print(f'{k:^10} {v:,}')

f = open('./day04/coffee.data','w') 
json.dump(coffee,f)
f.close()