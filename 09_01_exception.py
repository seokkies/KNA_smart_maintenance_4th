# #실습 2
# try:
#     temp = int(input("온도를 입력하세요: "))
#     print("정상적으로 입력되었습니다.")
# except:
#     print("숫자를 입력하세요")

# print("잘못 입력했어도 프로그램은 계속 실행됩니다.")

#실습 3
value = input("측정값을 입력하세요: ")
try:
    print(100 / int(value))
except ValueError:
    print("입력값이 숫자가 아닙니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")