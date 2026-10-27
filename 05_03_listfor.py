#실습 1
temp_list = [32, 21, 35, 31 ,29]
for i in range(len(temp_list)):
    if temp_list[i] >=30:
        print("고온:",temp_list[i],"/ ",end="")
print()

#실습 2
act_time = [8, 1, 6, 10, 5, 9, 1, 11]
for i in range(len(act_time)):
    if ((act_time[i] >= 5) and (act_time[i] <= 10)):
        print(act_time[i],"/ ",end="")
print()

#실습 3
temp_list = [32, 21, 36, 31 ,29]
total = 0
count = 0
print("(",end="")
for i in range(len(temp_list)):
    if temp_list[i] > 30:
        total = total + temp_list[i]
        count = count + 1
        print(temp_list[i],"",end="")

print(f" -> 합 {total}, 개수 {count}) 고온 평균: {(total/count):.1f}")

#실습 4
temp_list = [32, 21, 35, 31 ,29]
empty_list =[]
for i in range(len(temp_list)):
    if temp_list[i] > 30:
        empty_list.append(temp_list[i])
print(f"{empty_list} / 개수 {len(empty_list)}")

#실습 5
temp_list = [32, 21, 35, 31 ,29, 33]
empty_list =[]
for i in range(len(temp_list)):
    empty_list.append(round((temp_list[i] * 1.8),2) + 32)
print(empty_list)

#실습 6
temp_list = [32, 21, 35, 31 ,29, 33]
empty_list =[]
total = 0
total2 = 0
for i in range(len(temp_list)):
    total = total + temp_list[i]
    if temp_list[i] > 30:
        empty_list.append(temp_list[i])
        total2 = total2 + temp_list[i]
print(f"전체 평균: {(total/len(temp_list)):.2f} / 고온 개수: {len(empty_list)} / 고온 평균 {(total2/len(empty_list)):.2f}")
