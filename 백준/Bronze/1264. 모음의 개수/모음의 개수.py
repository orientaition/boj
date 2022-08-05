if __name__ == '__main__':
    v = ['a','e','i','o','u']
    while True:
        s = input().lower()
        if s == '#':
            break
        cnt = 0
        for i in s:
            if i in v:
                cnt += 1
        print(cnt)