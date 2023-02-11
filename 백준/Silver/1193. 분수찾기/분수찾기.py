x = int(input())
n = []
num = 0
count= 0

while count < x:
    num += 1
    count += num
count -= num

if num % 2 == 0:
    i = x - count
    j = num - i + 1
else:
    i = num - (x - count) + 1
    j = x - count

print(f"{i}/{j}")