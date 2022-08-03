def convert(list):
    dict = {list[i]: list[i+1] for i in range(0,len(list),2)}
    return dict
list = ['a',1,'b',2,'c',3,'d',4]
print(convert(list))
#with zip function
list_1=['a','b','c']
list_2=[1,2,3]
di=dict.fromkeys(list_1,"element")
print(di)
dz=dict(zip(list_1,list_2))
print(dz)