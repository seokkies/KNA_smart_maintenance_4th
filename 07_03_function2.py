#실습 1
def grade(temp=78, limit=80):
    if temp > limit:
        print(temp,"->","경고")
    else:
        print(temp,"->","정상")
grade() # default
grade(95)
grade(50, limit=49) 
print()

#실습 2
x = 10
def change():
    y = 30
    print(y)
change()
# print(y) #NameError: name 'y' is not defined 
print()

#실습 3
def get_average(values):
    return sum(values) / len(values)

def printer(x):
    if x < 90:
        print("정상:",avg)
    else:
        print("경고:",avg)

avg = get_average([75, 88, 92])
printer(avg)
print()