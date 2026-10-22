#실습 1
number = '01012345678'
print(len(number))

#실습2
message = '설비 고장 발생'
print('고장' in message,'/','정상' in message )

#실습3
stat = 'sensor-01-temp'
print(stat.count('-'))

#실습4
word = 'temp_2024'
print(word.find('_'),'/',word.find('a'))

#실습5
check = 'sensor_log.csv' 
print(check.startswith('sensor'),'/',check.endswith('csv'))

#실습6
label = 'WARNING'
print((label == 'WARNING'),'/',(label == 'warning'))