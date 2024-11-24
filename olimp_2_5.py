N = int(input())

count = 0
k = 1

while True:
    t = N - k * (k - 1) // 2
    if t <= 0:
        break
    if t % k == 0:
        a = t // k
        if a >= 1:
            count += 1
    k += 1

print(count)