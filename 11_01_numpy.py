#실습 1
import numpy as np
F = 'data/11_diecasting_series.csv'
ct = np.genfromtxt(F,
                    delimiter=',', # 값을 나누는 기호
                    skip_header=1, # 첫 줄(제목)은 건너뜀
                    usecols=(0, 1), #시점 사이클타임
                    encoding='utf-8') 
print(np.argmax(ct[:,1])) #인덱스 발생 위치
indexnum = np.argmax(ct[:,1])
print("시점:",ct[indexnum,0],"인덱스로 찾은 최대값:", ct[indexnum,1], "/" ,"max로 찾은 최대값:", np.max(ct[:,1]))

#실습 2
diff = np.diff(ct[:,1])
print(diff.size) #49개로 변한거 확인
print(np.argmax(np.abs(diff))) #급증 구간 확인
j = np.argmax(np.abs(diff))
indexnum = ct[j,0]
print(f"{indexnum}번과 {indexnum+1}번 사이에서 {diff[j]}초만큼 변함")