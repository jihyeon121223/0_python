import coffeetestfunc1 as ctf
##커피자판기 메뉴입력 프로그램
coffee={'아메리카노':3000} #읽어왔는데 커피 제 정의하면 오류나니깐
coffee=ctf.data_load('./day04/coffee.data')

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
        coffee = ctf.data_input(coffee)
    elif menu == '2':
        coffee =ctf.data_delete(coffee)
    elif menu=='3':
        coffee =ctf.data_update(coffee)
    elif menu=='4':
        ctf.data_list(coffee)
ctf.data_save(coffee)
