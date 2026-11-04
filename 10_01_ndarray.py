#실습 1

import numpy as np
temp = np.array([70, 71, 72, 73, 74, 75]) #반복문 없는 계산을 위해 array 사용
temp_tf = (temp*1.8 + 32)
print(temp_tf)

#실습 2
print(np.linspace(0, 70, 8))

#실습 3
print(np.arange(0, 40, 5))

#실습 4
data = [[25.3, 1.2], [26.1, 1.5], [27.4, 1.8], [28.2, 2.1]]  #온도, 전류
arr = np.array(data)
print(f"차원 개수: {arr.ndim} 행열 크기: {arr.shape} 값개수: {arr.size} 자료형: {arr.dtype}") 

#실습 5
elect = [18.69, 21.45, 23.87, 19.32] #전류
arr = np.array(elect)
print(f"차원 개수: {arr.ndim} 행열 크기: {arr.shape} 값개수: {arr.size} 자료형: {arr.dtype}")
arr_int = arr.astype(int)
print(arr_int)

#실습 6
cycle_time = [42.5, 43.2, 41.8, 44.1, 42.9, 43.7, 45.2, 41.5, 42.3, 44.6, 43.1, 42.7]

arr = np.array(cycle_time)
arr_re = arr.reshape(3,4)
print(arr_re)

#실습 7
sensor_data = [
    25.3, 1.2, 1450,
    26.1, 1.5, 1480,
    27.4, 1.8, 1520,
    28.2, 2.1, 1550
]
arr = np.array(sensor_data)
arr_re = arr.reshape(4,3)
print(arr_re)
print(arr_re.flatten())
