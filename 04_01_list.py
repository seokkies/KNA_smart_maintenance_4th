#실습 1
list1 = [25, 26, 24, 27, 26]
empty1 = []
print(list1,'/',len(list1),'/',len(empty1))

#실습 2
temp_list = [22, 23, 27, 25, 26, 23]
print(temp_list[0],',',temp_list[2],',',temp_list[-1])

#실습 3
val = [110,112,113,114,115,112]
fst = val[0]
last = val[-1]
print((fst+last),'/',(fst+last)/2)

#실습 4
temp = [22, 24, 27,1,2,3,4,28,30,21]
print(temp[0:3],'/',temp[-3:],'/',len(temp[0:3]))

#실습 5
list1 = [3,4,5,6,5,4,6,7,8,7,5,3]
fst = list1[0:6]
last = list1[6:]
print(fst,'/',last,'/',len(fst),len(last))

#실습 6
temp_list = [25, 26, 240, 28,27]
print(240 in temp_list)
temp_list[2] = 24
print(temp_list,'/',240 in temp_list)

#실습 7
a = []
a.append(30)
print(a)
a.insert(0,28)
print(a)
b=[31,32]
a.extend(b)
print(a)

#실습 8 
a = [24, 26, 24, 28, 26, 999]
a.remove(999)
print(a)
rm = a.pop(1)
print("꺼낸 값", rm)
del a[0]
print(a)

#실습 9
temp = [30,22,24,28,24,27,26]
temp.sort()
print(temp)
temp.reverse()
print(temp)
print(temp.count(24),'/',temp.index(24))