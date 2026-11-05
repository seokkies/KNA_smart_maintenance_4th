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
data = np.array([
    [int(row[4]), int(row[5])]
    for row in rows[1:15]
])

print("세 번째 시점:", data[2])
print("회전수:", data[:, 0])
print("토크:", data[:, 1])

#실습 3
rot = [i for i in range(0, 10)]
arr = np.array(rot)
print(arr)
print(f"최대: {arr.max()} 최소: {arr.min()}")
diff = arr.max() - arr.min()
norm = (arr - arr.min()) / diff
print(np.round(norm, 2))

#실습 4
data = np.array([
    [float(row[3]), int(row[4])] #전류, 회전 수
    for row in rows[1:]
])
empty =[]
total = 0
data[:,0] #전류
data[:,0] #회전 수
for row in data:
    total = total + 1
    if row[1] < 2000:
        empty.append([row[0], row[1], True])
    else:
        empty.append([row[0], row[1], False])
empty = np.array(empty)
print("저회전 비율:", np.sum(empty[:,2])/total * 100,"%")

empty =[]
total = 0
for row in data:
    total = total + 1
    if row[1] < 2000 or row[0] > 25 :
        empty.append([row[0], row[1], True])
    else:
        empty.append([row[0], row[1], False])
empty = np.array(empty)
print("저회전 또는 고전류 비율:", np.sum(empty[:,2])/total * 100,"%")

#실습 4-1
data = np.array([
    [float(row[3]), int(row[4])]
    for row in rows[1:]
])

# 저회전 비율 
condition1 = np.where(data[:, 1] < 2000, True, False)
print("저회전 횟수와 비율:", np.sum(condition1), "회", np.sum(condition1) / len(data) * 100, "%")

# 저회전 또는 고전류 비율
condition2 = np.where((data[:, 1] < 2000) | (data[:, 0] > 25), True, False)
print("저회전 또는 고전류 횟수와 비율:", np.sum(condition2), "회", np.sum(condition2) / len(data) * 100, "%")

#실습 5
tok = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12]
tok = np.array(tok)
condition = np.where(tok > 10, True, False)
print("토크 10초과 횟수와 비율:", np.sum(condition), "회", np.sum(condition) / len(tok) * 100, "%")

#실습 6
data = np.array([
    [float(row[4]), int(row[5])]
    for row in rows[1:]
])
print("회전수, 토크 평균:", np.average(data, axis=0)) #회전수, 토크 평균
print("회전수, 토크 표준편차:", np.round(np.std(data, axis = 0),1)) #회전수, 토크 표준편차
#이 경우 행이 2개이기 때문에 결과값 2개

#실습 7
rpm = np.loadtxt('data/10_mct_tool_18_261104.csv',
                    delimiter=',', # 값을 나누는 기호
                    skiprows=1, # 첫 줄(제목)은 건너뜀
                    usecols=4, # 5번째 열 = 회전수
                    encoding='utf-8') 
print("회전 수 평균:", np.round(np.mean(rpm), 1), "회전 수 표준편차:", np.round(np.std(rpm)), 1)
print("회전 수 최소:", np.min(rpm), "회전 수 최대:", np.max(rpm)) 
#특이값의 경우 표준편차를 고려해도 극도로 거리가 멀기 때문에 고장의 징후일 확률이 높다 사료됨

#실습 8
rpm = np.loadtxt('data/10_mct_tool_18_261104.csv',
                    delimiter=',', # 값을 나누는 기호
                    skiprows=1, # 첫 줄(제목)은 건너뜀
                    usecols=5, # 6번째 열 = 토크
                    encoding='utf-8')
tok = rpm[rpm > 10]
print(tok)
print("10초과 값 개수:", np.size(tok))
print("값 평균:" , np.round(np.mean(tok), 1))

#실습 9
rpm = np.loadtxt('data/10_mct_tool_18_261104.csv',
                    delimiter=',', # 값을 나누는 기호
                    skiprows=1, # 첫 줄(제목)은 건너뜀
                    usecols=(4,5), # 6번째 열 = 토크
                    encoding='utf-8')
print(rpm.shape, rpm.dtype)
rot = rpm[rpm[:,0] < 2000]
print(np.size(rot[:,0]), np.mean(rot[:,0]), np.mean(rpm[:,0]) )