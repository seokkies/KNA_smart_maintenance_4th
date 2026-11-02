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

#실습 5
import csv

with open("data/output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "온도", "습도"])
    writer.writerow(["센서A", 25, 60])
    writer.writerow(["센서B", 30, 55])
    writer.writerow(["센서C", 28, 70])
with open("data/output.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   

#실습 6
import csv
with open("data/08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    result = []
    for row in reader:
        if float(row[4]) > 90:
            result.append(row)

with open("data/output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["설비ID", "시각", "진동X", "진동Y", "전류", "상태"])
    writer.writerows(result)
with open("data/output.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   