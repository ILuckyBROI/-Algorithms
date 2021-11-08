import tracemalloc

tracemalloc.start()
def fun():
    a = [0] * 8
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                a[j - 2] += 1
    i = 0
    while i < len(a):
        print(i + 2, ' - ', a[i])
        i += 1

fun()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print('Статистика:')
for stat in top_stats[:10]:
    print(stat)
