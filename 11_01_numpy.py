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

#실습 3
import numpy as np

F = 'data/11_diecasting_series.csv'

cyl = np.genfromtxt(F,
                    delimiter=',',
                    skip_header=1,
                    usecols=2,
                    encoding='utf-8')
cyl[0] = 9999

print("보정 전 평균:", np.mean(cyl))
fixed = np.clip(cyl, 100, 300)
print("보정 후 평균:", np.mean(fixed))

# 실습 4
import numpy as np

F = 'data/11_diecasting_series.csv'
ct = np.genfromtxt(F,
                   delimiter=',',
                   skip_header=1,
                   usecols=1,
                   encoding='utf-8')

status = np.where(ct >= 1000, 2, np.where(ct >= 50, 1, 0))

kinds, counts = np.unique(status, return_counts=True)
ratio = counts / ct.size

print("상태 번호:", kinds)
print("상태별 개수:", counts)
print("상태별 비율:", ratio)

#실습 5
import numpy as np

F = 'data/11_diecasting_series.csv'

cyl = np.genfromtxt(F,
                    delimiter=',',
                    skip_header=1,
                    usecols=(1,2,3,4),
                    encoding='utf-8')
print(cyl[:,0])
arr_stack = np.stack([cyl[:,0],cyl[:,1],cyl[:,2],cyl[:,3]])
print(arr_stack.shape)
arr_recent = arr_stack[:,-10:]
print(arr_recent.shape)

#실습 6
import numpy as np
F = "data/11_diecasting_series.csv"
cyl = np.genfromtxt(F,
                    delimiter=',',
                    skip_header=1,
                    usecols=(0, 1, 2),
                    encoding='utf-8')

i = np.argmax(cyl[:,1]) #최대 시점의 인덱스 넘버
print(f"최대 시점: {cyl[i,0]} / 최대값: {cyl[i,1]}")

j = np.argmax(np.diff(cyl[:,1])) #차이값의 최대 지점
print(f"급변 구간 {cyl[j,0]} -> {cyl[j+1,0]}")

status = np.where((cyl[:,1]>=50) | (cyl[:,2]<150), True, False)
print("경고 비율:", np.sum(status) / len(cyl))


sorted_cyl  = np.argsort(cyl[:,1],descending=True) #사이클 내림차순 정렬하고
print("상위 3개 시점: ",cyl[sorted_cyl[:3],0])
print("상위 3개 시점 값: ",cyl[sorted_cyl[:3],1])
