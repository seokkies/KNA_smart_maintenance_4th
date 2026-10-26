#실습 1 
age = 30
if age>=19:
    print("성인입니다.")
else:
    print("미성년자입니다.")

#실습 2
score = 75 #int(input("점수를 입력하세요: "))
if score >= 90:
    print("A등급")
elif score >=80:
    print("B등급")
elif score >=70:
    print("C등급")
else: print("F등급")

#실습3
for i in range (3):
    temp = 75 #int(input("온도를 입력하세요: "))
    if temp > 80:
        print("위험")
    elif temp > 60:
        print("주의")
    else: print("정상")

#실습 4
true_idntt = "true_idntt"
true_password = "true_password"
idntt = input("id를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

if ((true_idntt == idntt) and (true_password == password)) :
    print(idntt ,'/', password, "로그인 성공")
else:
    print(idntt ,'/', password, "로그인 실패")
