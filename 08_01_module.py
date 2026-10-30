# 실습 1

import math
result = math.sqrt(16)
print(result)

from math import sqrt
result = sqrt(16)
print(result)

import math as mt
result = mt.sqrt(25)
print(result)
print()

#실습 2
import random
import math

sensor = random.randint(1, 100)
print("센서값:", sensor)

result = math.sqrt(sensor)
print("제곱근:", result)
print()

#실습 3
import os
count = 0
empty =[]
cwd = os.getcwd()
print("현재 작업중인 폴더:", cwd)
files = os.listdir(cwd)

for name in files:
    print(name) #전체 출력
    if name.endswith(".csv"): #csv만 골라 출력
        count = count + 1
        empty.append(name)

if count == 0 :
    print("현재 작업중인 폴더에 csv 파일 없음")
else:
    print("csv 파일 목록:",empty)

print()

#실습 4
import os
path = os.path.join("data", "08_press.csv")
if os.path.exists(path):
    print('파일 있음:', path)
print()


#실습 5
import os
import datetime as dt
count = 0
cwd = os.getcwd()
files = os.listdir(cwd)
for name in files:
    count = count + 1
time = dt.datetime.now()
print(f"파일 {count}개, 점검 시각 {time}")
print()

#실습 6
import os
empty = []
cwd = os.getcwd()
files = os.listdir(cwd)

for name in files:
    if name.endswith(".csv"):
        full_path = os.path.join(cwd, name)
        empty.append(full_path)

if len(empty) == 0:
    print("현재 작업중인 폴더에 csv 파일 없음")
else:
    print("csv파일경로: ",empty)