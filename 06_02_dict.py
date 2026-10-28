# 실습 1
sensors = {"모터온도": 78, "진동": 0.5}
print(sensors["모터온도"])
sensors["펌프압력"] = 95
sensors["진동"] = 0.8
print(sensors)
print(sensors.get("습도", 0))
print("모터온도" in sensors)
print()

#실습 2
sensors = {"모터온도": 78, "진동": 0.5}
new_dict = {"펌프압력": 95, "진동": 0.8}
sensors.update(new_dict)
print(sensors, "센서 수:", len(sensors))
del sensors["모터온도"]
print(sensors, "센서 수:", len(sensors))
print()

#실습 3
sensors = {"모터온도": 78, "진동": 0.5}
total = 0
max = 0
max_name =""
for name, value in sensors.items():
    total = total + value
    if value > max:
        max = value
        max_name = name
print("평균:", total/len(sensors))
print("최대값 센서:", max_name,max)
print()

#실습 4
name = ["모터온도", "펌프압력", "진동", "습도"]
value = [75, 95, 0.6, 5]
dict1  = dict(zip(name,value))
print(dict1)
for name, value in dict1.items():
    print(name, value)
print()

#실습 5
sensors = {"모터온도": 78, "진동": 0.5, "펌프압력": 95, "습도":1}
limit_sensors = {"모터온도": 75, "진동": 2, "펌프압력": 120, "습도":0.8}
for name, value in sensors.items():
    if value > limit_sensors[name]:
        print("경고 센서: ",name)
print()

#실습 6
plant = { 
"1번모터": {"온도": 78, "상태": "정상"}, 
"2번펌프": {"압력": 95, "상태": "경고"}, 
"3번진동": {"진동": 2.1, "상태": "경고"}
} 
#압력 꺼내기
print(plant["2번펌프"]["압력"])
for name, stat in plant.items():
    if stat["상태"] == '경고':
        print(name, "점검 필요")
print()

#실습 7
sensors = ["모터온도,78", "진동,0.5", "펌프압력,95", "습도,1"]
sensor_dict = {}
for i in range(len(sensors)):
    name, value = sensors[i].split(',')
    sensor_dict[name] =  value
print(sensor_dict)
print()

#실습 8
sensors = {"모터온도": 78, "진동": 0.5, "펌프압력": 95, "습도":1}
limit_sensors = {"모터온도": 75, "진동": 2, "펌프압력": 120, "습도":0.8}
over_sensors = set() 
total = 0

for name, value in sensors.items():
    total = total + value
    if value > limit_sensors[name]:
        over_sensors.add(name)
print("평균:",total/len(sensors))
print("위험 센서:", over_sensors)
print()