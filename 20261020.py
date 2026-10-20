print("안녕하세요")
print(75)

#print는 파이썬에 기본으로 들어있는 내장함수
#
print("안녕하세요")
print("첫 번째 줄")
print("두 번째 줄")

print("온도")
print(75)
print("진동")
print(2.3)

#날짜 출력하기
from datetime import datetime

now = datetime.now()
print(now.strftime("%y%m%d"))
print(now.strftime("%y%m%d%H%M"))

#문자출력
print("안녕하세요")
print("저는 설비 데이터를 배웁니다")

#쉼표는 띄어쓰기가 들어감
print("온도", 75) 
print("온도(℃):", 75)
print("=== 1번 설비 측정값 ===")

#1번 설비 측정값 출력
print("온도(℃):", 75) #정상 범위
print("진동(mm/s):", 2.3) #정상 범위

print(75 + 5)
print(82 - 75)

print(" 두 측정값의 합:", 75 + 80) 
print(" 온도 변화량:", 82 - 75) 
print(" 평균 온도:", (75 + 80) / 2)

print("정상 온도:", 71)
print("현재 온도:", 82)
print("차이 계산 직전:", 82, 71)  
print("온도 상승량:", 82 - 71)
#주석 달아

#NameError 만들어서 수정하기
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# /tmp/ipykernel_4363/1278121386.py in <cell line: 0>()
# ----> 1 print(NameError만들기)
#       2 # 메시지에서 line, NameError, not defined
#       3 # print("NameError 만들기")

# NameError: name 'NameError만들기' is not defined
# 메시지에서 line, NameError, not defined 
print("NameError 만들기")


#SyntaxError 만들어서 수정하기
print("온도")
#   File "/tmp/ipykernel_4363/1023331850.py", line 1
#     print("온도)
#           ^
# SyntaxError: unterminated string literal (detected at line 1)
print("진동")
#   File "/tmp/ipykernel_4363/2601263756.py", line 7
#     # SyntaxError
#                  ^
# _IncompleteInputError: incomplete input

#3개 오류 수정하기
print("온도", 75)
print("진동", 2.3)
print("압력", 4.0)

temp = 25 # 숫자 저장
name = "센서A" # 글자는 따옴표
count = 3 # 숫자 저장

temp = 25
print(temp) # 25 (값)
print("temp") # temp (글자)

x = 10
print(x) # 10
x = 20
print(x) # 20

temp = 25
Temp = 100
print(temp) # 25
print(Temp) # 100

temp = 25
temp = 30 # 30으로 교체

x = 10
x = 20
x = 30
print(x) # 30

a = 10 # a에 10 저장
b = a # 10 복사
a = 99
print(b) # 10 (그대로!)

x, y, z = 10, 20, 30
print(x) # 10
print(y) # 20

temp = 25 # 온도(섭씨)
count = 3 # 센서 개수
# temp = 100 # 실행 안 함

#실습1
temp = 25  #temp에 25 저장
print(temp)
name = "센서A" #name 변수에 센서A라는 문자 저장
print(name)

#실습2
temp = 30
temperature = temp
print(temperature)

#실습3
my_number = 777
print(my_number)
mood = "lucky"
print(mood)

#실습4
age = 30
label = "나이"
print(label, age)

#실습5
x = 10
print(x)
x = x + 5
print(x)
x = x*2
print(x)

#실습6
a = 100
b = a
a = 999
print(a, b)

#실습 7
# print(temp1)
# Traceback (most recent call last):
#   File "c:\vscode file\20261020.py", line 154, in <module>
#     print(temp1)
#           ^^^^^
# NameError: name 'temp1' is not defined. Did you mean: 'temp'?
temp1 = 25
print(temp1)
score = 90
# print(Score)
# Traceback (most recent call last):
#   File "c:\vscode file\20261020.py", line 162, in <module>
#     print(Score)
#           ^^^^^
# NameError: name 'Score' is not defined. Did you mean: 'score'?
print(score)

#실습8
temp = 25 #온도(섭씨)
count = 3 #센서 개수
# temp = 100
print(temp)

#실습9
x = 5
x = 10 #현재 10
x = x + 1 #현재 11
print(x) # 10 + 1 이므로 11 추정


#실습10
name = "센서A"
temp = 25
count = 10 # 설비이름, 온도, 점검횟수
print(name, temp, count)

#실습11
a = 25
b = 3 #아무 상수
device_temp = a
sensor_count = b #기기온도와 센서개수 의미부여
print(device_temp, sensor_count)

#실습12
x,y,z = 1,2,3
width, height = 4, 3
print(width, height)