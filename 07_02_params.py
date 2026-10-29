#실습 1
def report(name, temp):
    print(f"{name} {temp} 도")

report("모터", 78)
report("펌프", 92)
report(78, "모터")
print()

#실습 3
def report(name, temp):
    print(name, temp)
report(name="모터", temp=78)
report(temp=92, name="펌프")
print()

#실습 4
def add(x,y):
    return x + y
a = 40
b = 45
c = add(a,b)
print(c)
print(c+5)
print()

#실습 5
def sensor_stats(values):
    min_val = min(values)
    max_val = max(values)
    avg_val = sum(values) / len(values)
    return min_val, max_val, avg_val

sensors = [78, 92, 85, 86, 84]
minimum, maximum, average = sensor_stats(sensors)
print(minimum, maximum, average)