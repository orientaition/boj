import sys
input = sys.stdin.readline
def a(target, data) -> str:
    return 'Yes' if target == sum([x[0] * x[1] for x in data]) else 'No'
if __name__ == '__main__':
    x = int(input())
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    print(a(x, data))