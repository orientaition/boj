score = input()
res = 0
if score[0] =='A':
    res += 4
elif score[0] =='B':
    res += 3
elif score[0] =='C':
    res += 2
elif score[0] =='D':
    res += 1
if score =='F':
    res = 0
elif score[1] =='+':
    res += 0.3
elif score[1] =='-':
    res -= 0.3
print(float(res))