n = list(map(int,input().split()))
result = [1,2,3,4,5,6,7,8]
if n == result:
    print('ascending')
elif n == result[::-1]:
    print('descending')
else:
    print('mixed')