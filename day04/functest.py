def add(x,y):
    return x+y

# a=1
# b=2
# result=add(y=a,x=b)
# print(result)

# a='aaa'
# b='bbb'
# result=add(a,b)
# print(result)


def add_many(*x):
    print(x)
    result=0
    for i in x:
        result += i
    return result

data=add_many(1,2,3,4,5,6,7,8,9,10)
print(data)