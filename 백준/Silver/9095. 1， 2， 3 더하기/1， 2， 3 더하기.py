t = int(input())
number = [1,2,4]
for i in range(3,10):
    number.append(number[i-3] + number[i-2] + number[i-1])
for i in range(t):
    n = int(input())
    print(number[n-1])