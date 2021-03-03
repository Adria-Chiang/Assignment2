def calculate(min, max):
    ans = 0
    for i in range(min, max + 1):
        ans += i
    print(ans)

calculate(4, 8)