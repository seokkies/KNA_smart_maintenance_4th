#실습 1
sensor = ("모터온도", 78)
print(sensor[0],sensor[1])
name, value = sensor
print(name, value)

#실습 2
sensors = [("모터온도", 78), ("회전속도", 92), ("펌프입력", 95)]
for name, value in sensors:
    if value > 90:
        print(name, "경고")

#실습 3
sensors = [("모터온도", 78, (3,5)), ("회전속도", 92, (7,6)), ("펌프입력", 95,(5,3))]
empty_list =[]
for name, value, xy in sensors:
    print(name, xy)
    if xy[0] <= 5:
        empty_list.append(name)
print(empty_list)