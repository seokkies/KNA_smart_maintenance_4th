#실습 1
import numpy as np

F = "data/11_hydraulic_cooler.csv"
vib = np.genfromtxt(F,
                    delimiter=",",
                    skip_header=1,
                    usecols=2,
                    encoding="utf-8")
print("결측치 개수:", np.sum(np.isnan(vib))) # 결측치 개수
print("결측치 비율:", np.sum(np.isnan(vib)) / len(vib))
print("결측치 무시 평균:", np.round(np.nanmean(vib), 3))
print("결측치 포함 평균:", np.mean(vib))

#실습 2
import numpy as np

F = "data/11_hydraulic_cooler.csv"
vib = np.genfromtxt(F,
                    delimiter=",",
                    skip_header=1,
                    usecols=1,
                    encoding="utf-8")

q1, q3 = np.percentile(vib, [25, 75])
iqr = q3 - q1
upper = q3 + (iqr * 1.5)
over_temp = np.where(vib > upper)
print(f"상한: {np.round(upper, 1)} / 특이값: {vib[over_temp]} / 특이값 개수: {len(over_temp[0])}")

#실습 3
import numpy as np

F = "data/11_hydraulic_cooler.csv"
vib = np.genfromtxt(F,
                    delimiter=",",
                    skip_header=1,
                    usecols=(0,1),
                    encoding="utf-8")

temp = vib[:,1]
mean = np.mean(temp)
std = np.std(temp)
print(f"온도 평균: {mean} / 온도 분산: {std}")
z = (temp - mean) / std
print("최대 z값:", np.round(np.max(z), 2))
over_temp = np.where(np.abs(z) > 2)
print(vib[over_temp,0][0])


#실습 4
import numpy as np

F = "data/11_hydraulic_cooler.csv"
vib = np.genfromtxt(F,
                    delimiter=",",
                    skip_header=1,
                    usecols=(0,1),
                    encoding="utf-8")

temp = vib[:,1]
mean = np.mean(temp)
std = np.std(temp)
print(f"온도 평균: {mean} / 온도 분산: {std}")
upper = mean + 3*std
print("상한: ", np.round(upper, 2))
over_temp = np.where(temp > upper)
print(vib[over_temp,0][0])

#실습 5
import numpy as np

F = "data/11_hydraulic_cooler.csv"
vib = np.genfromtxt(F,
                    delimiter=",",
                    skip_header=1,
                    usecols=(1,3), #온도 / 냉각효율
                    encoding="utf-8")

temp = vib[:,0]
cooling = vib[:,1]
coef = np.corrcoef(temp, cooling)
print(np.round(coef[0,1], 2)) # 온도가 1 상승하면 냉각효율이 0.99떨어짐

#실습 6
import numpy as np

F = "data/11_hydraulic_cooler.csv"
data = np.genfromtxt(F,
                    delimiter=",",
                    skip_header=1,
                    usecols=(1,2,3,4), #온도 / 냉각효율
                    encoding="utf-8")
temp = data[:,0]
vib = data[:,1]
cooling = data[:,2]
cooling_power = data[:,3]

reverse = np.array([temp, vib, cooling, cooling_power])
print("센서별 평균:",np.round(np.nanmean(reverse, axis=1), 1))
print("센서별 편차",np.round(np.nanstd(reverse, axis=1), 1))

#실습 7
import numpy as np

F = "data/11_hydraulic_cooler.csv"
data = np.genfromtxt(F,
                    delimiter=",",
                    skip_header=1,
                    usecols=(0,1), #시점 온도
                    encoding="utf-8")
cyl = data[:,0]
temp = data[:,1]
mean_temp = np.mean(temp)
print("온도 전체 평균: ", mean_temp)
cs =  np.cumsum(temp - mean_temp)
print(cyl[np.argmin(cs)])

#실습 8
import numpy as np

F = "data/11_hydraulic_cooler.csv"
data = np.genfromtxt(F,
                    delimiter=",",
                    skip_header=1,
                    usecols=(0,1,3,5), #시점 / 온도 / 냉각효율 / 상태
                    encoding="utf-8")
cyl = data[:,0]
temp = data[:,1]
cooling = data[:,2]
stat = data[:,3]

temp_z = np.abs(temp - np.mean(temp)) / np.std(temp)
cooling_z =  np.abs(cooling - np.mean(cooling)) / np.std(cooling)
score = temp_z + cooling_z
t = np.argmax(score)
print("점수가 가장 높은 시점:", cyl[t], np.round(score[t], 2))
print("상위 세 시점: ", cyl[np.argsort(score)[-3:][::-1]])