#실습 1
name = "PUMP_A"
temp = "87도"
print(f"설비 {name} 온도 {temp}")

#실습 2
a = 86
b = 87
c = 88
print(f"평균 {(a+b+c)/3}")

#실습 3
value = 87.456
print(f"{value:.1f} / {value:.2f}")

#실습 4
word = '  5 , sensor_2 , WARNING , 0.78912  ' 
str = word.strip().split(',')
sensor = str[1].strip()
stat = str[2]
value = str[3]
print(f"[센서 {sensor}] 상태 {stat.lower()}, 측정값 {float(value):.2f}")