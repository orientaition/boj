n = int(input())
cnt = 0
a = n
while True:
    cnt +=1
    sum = n//10 + n%10
    n = n%10*10 + sum%10
    if(n == a):
        break
print(cnt)