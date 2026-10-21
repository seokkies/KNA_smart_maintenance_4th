#실습1
count = 3 #(개수·나이)
temp =  25.5 #(온도·평균)
name = "센서A" #(이름·상태)
is_ok = True #(참·거짓)
print(count, temp, name, is_ok)

#실습2
print(type(count), type(temp), type(name), type(is_ok))

#실습3
a = 100 #int로 예측
b = 100.1 #float으로 예측
c = "100" #str로 예측
print(type(a), type(b), type(c))

#실습4
print(1+2)
print("1"+"2")
print("11"+"22")

#실습5
bool(3>2) #당연히 참이므로 True
bool(5==5)#당연히 참이므로 True
print(type((3>2)), type((5==5))) #bool type이니 bool이 나오겠죵

#실습6
count = 10
print(type(count))
count = 10.1
print(type(count))
count = "str"
print(type(count))

#실습7
device_temp = 36.5
check_count = 11
device_name = "가나다라"
is_normal = False
print(device_temp,check_count,device_name,is_normal)


#=========================================

#실습1
a = 17
b = 5
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

#실습2
a = 7
b = 3
c = 5
mean = (a+b+c)/3
s2 = a^2
v3 = a*b*c
print(mean, s2, v3)

#실습3
print(1==1, 1!=2, 1>2, 1<2, 2>=1, 2<=1)

#실습4
temp = 80
is_temp = (60<=temp<=90)
press = 5
is_press = (3<=press<=7)
print(is_temp, is_press, is_press and is_temp)

#실습5
a = 100
print(a)
a += 50
print(a)
a -= 30
print(a)
a += 5
print(a)

#실습6
rate1 = 23/500*100
rate2 = 21/24*100
print(rate1, rate2)


#실습7
print(f'{500//60}시간 {500%60}분')

# #실습1
# year = int(input("출생연도를 입력하세요: "))
# age = 2026-year+1
# print(age)

# #실습2
# nation = (input("거주국가를 입력하세요: "))
# city = (input("거주도시를 입력하세요: "))
# print(f'{nation}의 {city}에 거주하는중입니다.')

# #실습3
# a = float(input("수1: "))
# b = float(input("수2: "))
# print("합:", a + b)
# print("차:", a - b)
# print("곱:", a * b)
# print("나눗셈:", a / b)

# #실습4
# temp =  float(input("온도: "))
# print("80 이상?", temp >= 80)
# print("80 미만?", temp < 80)

# x = int(input("국어: "))
# y = int(input("수학: "))
# z = int(input("영어: "))
# avg = (x + y + z) / 3
# print("평균점수 60 이상", avg >= 60)
# print("평균점수 60 미만", avg < 60)

#실습1
a = '''가동 점검표/
1. 온도 확인/
2. 압력 확인
'''
print(a)

#실습2
a = "PUMP_A" 
b = "정상"
c = "2025-01-15"
print(a+"/"+b+"/"+c)

# 실습3
code = "PUMP_B" #코드
stat = "정상" #상태
act_time = 9 #가동시간
check_date = "2026-10-21" #점검일

print(code +'/'+stat+'/'+ str(act_time) +'/'+ check_date)
