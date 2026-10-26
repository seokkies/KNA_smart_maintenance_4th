#실습 1
# a = int(input("정수를 입력하세요: "))
a = 5

for i in range(1, a+1):
    print(i,end="")
print()
for i in range(2, a+1,2):
    print(i,end="")
print()   
for i in range(a, 0 ,-1):
    print(i,end="")
print()

#실습 2
n = int(input("정수를 입력하세요: "))

total = 0
for i in range(1, n+1):
    total = total + i
print(f"(N = {n}) 합: {total}")

#실습 3
for i in range(2,10):
    print(f"{i}단")
    for j in range(1,10):
        print(f"{i}x{j}={i*j} ",end="")
    print()
    print("============================================================")

#실습4
num = int(input("측정 횟수를 입력하세요: "))
count = 0
for i in range(1, num+1):
    val = int(input("측정값을 입력하세요: "))
    if val>80:
        count = count + 1
print(f"({num}회 중 {count}개가 80초과) 초과 개수: {count}")

