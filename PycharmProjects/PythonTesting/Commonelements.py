list1=[1,2,3,4,5,6,7]
list2=[2,4,6,8,10,12]
common=list(filter(lambda x:x in list1,list2))
print(common)
common2=[item for item in list1 if item in list2]
print(common2)