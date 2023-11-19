n = int(input())
k = int(input())
m = [x for x in range(1, n + 1)]
kill = k - 1
while len(m) > 1:
    m.pop(kill)
    kill = (kill + k - 1) % (len(m))
print(m[0])