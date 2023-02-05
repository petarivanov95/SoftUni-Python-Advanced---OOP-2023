n, m = tuple(map(int, input().split()))

set1 = set()
set2 = set()

# for set #1
for x in range(n):
    entry = int(input())
    set1.add(entry)

# for set #2
for y in range(m):
    entry = int(input())
    set2.add(entry)

intersection = set1.intersection(set2)

for num in intersection:
    print(num)

