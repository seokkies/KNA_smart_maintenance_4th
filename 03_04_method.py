#실습 1
up = 'ready'
print(up.upper())

#실습 2
low = 'WARNING'
print(low.lower())

#실습 3
title = 'kim chul soo' 
print(title.title())

#실습 4
low = 'Fault'
up = 'FAULT'
print((low==up),'->',(low.lower()==up.lower()))

#실습 5
up = 'ABC'
mid = 'Abc'
low = 'abc'
print(up.isupper(),'/',low.islower(),'/',mid.isupper())

#실습 6
csv = 'Sensor_LOG.CSV'
print(csv.lower().startswith('sensor'),'/',csv.lower().endswith('.csv'))

#실습 7
str = ' 가동중 '
print('['+str.strip()+']')

#실습 8
str = ' 대기 '
print('['+str.lstrip()+']','/','['+str.rstrip()+']')

#실습 9
str = '***경고***'
print(str.lstrip('***').rstrip('***'))

#실습 10
str = ' WARNING '
print(str.strip().lower())

#실습 11
str = ' 경보 '
str.strip()
str1 = str.strip()
print('['+str+']','->','['+str1+']')