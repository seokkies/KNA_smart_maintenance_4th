import numpy as np
import csv

with open("data/10_mct_tool_18_261104.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)

#실습 1
rpm = [int(row[4]) for row in rows[1:11]]

arr = np.array(rpm)

print(f"맨 앞: {arr[0]} 맨 뒤: {arr[-1]}")
slide = arr[1:4]
print("2 ~ 4 구간:", slide)
print("1부터 1개씩 건너뛰기:", arr[::2])


#실습 2
# 실습 2. 한 시점과 한 센서 따로 꺼내기
data = np.array([
    [int(row[4]), int(row[5])]
    for row in rows[1:15]
])

print("세 번째 시점:", data[2])
print("회전수:", data[:, 0])
print("토크:", data[:, 1])