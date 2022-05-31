import json #파일을 왔다갔다 계속 쓸 때 씀

def data_load(path): 
    f = open(path,'r') #밑에꺼 먼저 하고 나중에 주석풀어서 읽기
    coffee=json.load(f) 
    f.close()
    return coffee

def data_input(coffee):
    item=input('메뉴>>>')
    price=int(input('가격>>>'))
    coffee[item]=price
    print(coffee)
    return coffee

def data_delete(coffee):
    print(coffee.keys())
    item = input('삭제할 메뉴명>>>')
    del coffee[item]
    print(coffee)
    return coffee

def data_update(coffee):
    print(coffee.keys())
    item=input('메뉴>>>')
    price=int(input('가격>>>'))
    coffee[item]=price
    print(coffee)
    return coffee

def data_list(coffee): #변경되지않기때문에 리턴안해줘
    for k,v in coffee.items():
        print(f'{k:^10} {v:,}')

def data_save(coffee):
    f = open('./day04/coffee.data','w') 
    json.dump(coffee,f)
    f.close()

