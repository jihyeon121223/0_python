import pickle #저장하고 읽어오는거 2가지

# f = open('./day04/pickle01.txt','wb') #w는 텍스트형태, b붙으면 그대로
# coffee={'아메리카노':3000}
# pickle.dump(coffee,f)
# f.close()

# f = open('./day04/pickle01.txt','rb')
# coffee=pickle.load(f) #loads는 파일형태
# f.close()
# print(coffee)

import json

# f = open('./day04/json01.txt','w',encoding='cp949') 
# coffee={'아메리카노':3000}
# json.dump(coffee,f)
# f.close()

f = open('./day04/json01.txt','r')
coffee=json.load(f) 
f.close()
print(coffee)