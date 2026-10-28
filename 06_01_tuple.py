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

#실습 4
sensor_id = ["S01","S01","S02","S03"]
unique_id = set(sensor_id)
print(sorted(unique_id), "종류 수:", len(unique_id))

#실습 5
sensor_id1 = set(["S01","S01","S02","S03","S05"])
sensor_id2 = set(["S04","S04","S05","S03"])
uni = sensor_id1.union(sensor_id2)   #sensor_id1 | sensor_id2
intersec = sensor_id1.intersection(sensor_id2)
diff1 = sensor_id1.difference(sensor_id2)
diff2 = sensor_id2.difference(sensor_id1)
print("전체:", uni )
print("교집합:", intersec)
print("A만:", diff1)
print("B만:", diff2)

#실습 6
sensor_today = {"S02","S03","S05"}
sensor_yesterday = {"S02","S03","S04"}
diff_today = sensor_today.difference(sensor_yesterday)
intersec = sensor_yesterday.intersection(sensor_today)
print("신규 이상:",diff_today)
print("지속 이상:",intersec)