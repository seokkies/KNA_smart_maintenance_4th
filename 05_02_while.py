#실습 1
x = 0
y = 10
while x != 7:
    x = int(input("추정값을 입력하세요: "))
    if x>7:
        print(x,"보다 작습니다.")
    elif x<7:
        print(x,"보다 큽니다.")
print("정답입니다.")

#실습 2
found = False
n = int(input("측정 횟수를 입력하세요: "))
for i in range(n):
    val = int(input("측정값을 입력하세요: "))
    if val > 80:
        found = True
        print("발견")
        break
if found == False:
    print("없음")