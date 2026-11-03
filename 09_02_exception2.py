# #실습 1
# import os

# f = open("data/09_ict_inspection_15_261102_1.csv","r",encoding="utf-8")
# try:
#     print(f.read())
#     0/0 #에러 발생시키기
# except:
#     print("에러가 발생했습니다")
# finally:
#     f.close()
#     print("파일을 닫습니다.")

# #실습 2
# import csv

# total = 0
# count = 0
# try:
#     with open("data/09_ict_inspection_15_261102_1.csv", "r", encoding="utf-8") as f:
#         reader = csv.reader(f)
#         next(reader)
#         for row in reader:
#             try:
#                 total += float(row[2])
#             except (ValueError, IndexError):
#                 count = count + 1
#                 continue

# except FileNotFoundError:
#     print("파일이 존재하지 않습니다.")

# print("측정값 합계:", total)
# print("기타 에러 발생 횟수:",count)

# #실습 3
# import csv
# total = 0
# count = 0
# count2= 0
# with open("data/09_ict_inspection_dirty_15_261102_2.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         try:
#             total = total + float(row[2])
#         except ValueError:
#             print("ValueError 발생")
#             count = count + 1
#             continue
#         except:
#             count2 += 1
#             print("기타 에러 발생")
#             continue
# print("측정값 합계:",total)
# print("ValueError 발생 횟수:",count)
# print("기타 에러 발생 횟수:",count2)

# #실습 4
# import os
# path = os.getcwd()
# files = os.listdir(path)
# count = 0
# count2 =0
# count3 = 0
# files.append("존재하지 않는 파일.py")
# for name in files:
#     try:
#         if name.endswith(".py"):
#             with open(name, "r", encoding="utf-8") as f:
#                     # reader = f.readlines()
#                     # print(reader)
#                 count += 1
#         else:
#             print(name,"은 py 파일이 아닙니다")
#             count2 += 1

#     except FileNotFoundError:
#         print(name, "파일이 없습니다.")
#         count3 +=1
#         continue

# print("처리한 파일 수:", count)
# print("조건에 맞지 않는 파일 수: ", count2)
# print("FileNotFoundError 발생 횟수:", count3)

# 실습 5
def check_value(value, min_value=0, max_value=5000):
    value = int(value)
    if value < min_value or value > max_value:
        raise ValueError("정상 범위를 벗어난 값입니다.")
    return value

try:
    value = input("값을 입력하세요: ")
    result = check_value(value)
    print(f"정상 입력값: {result}")

except ValueError as e:
    print(f"입력 오류: {e}")