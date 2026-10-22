#실습 1
word = '설비 정상 가동'
print(word.replace('정상','점검'))

#실습 2
word = 'PUMP A 03' 
print(word.split())

#실습 3
word = 'a,b,c,d' 
print(word.split(','))

#실습 4
word = 'a,b,c,d' 
print(word.split(',',1))

#실습 5
arr = ['2025','01','15'] 
print('-'.join(arr))

#실습 6
word = '2025·1·15'
arr = word.split('·')
print(*arr, sep='-', end=' / ')
print(*arr, sep=', ')

#실습 7
word ='2025/01/15' 
print('-'.join((word.split('/'))))

#실습 8
word ='1, NORMAL ,25.3' 
arr = word.split(',')
print(arr[1].rstrip().lstrip().lower())