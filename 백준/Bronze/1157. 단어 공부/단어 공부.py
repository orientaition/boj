w = input().upper()
w_l = list(set(w))
cnt = []
for i in w_l:
    count = w.count
    cnt.append(count(i))
if cnt.count(max(cnt)) > 1:
  print("?")
else:
  print(w_l[(cnt.index(max(cnt)))])