#실습 2
with open("data/text.txt", "w", encoding="utf-8") as f:
    f.write("쓰기 테스트")
with open("data/text.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
print()

#실습 3
with open("data/text.txt", "a", encoding="utf-8") as f:
    f.write(" + 추가로 쓰기 테스트")
with open("data/text.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
print()


#실습 4
import csv

with open("data/08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)