while True:
    num = input()
    if num == "0":
        break
    answer = "no"
    if num == num[::-1]:
        answer = "yes"
    print(answer)