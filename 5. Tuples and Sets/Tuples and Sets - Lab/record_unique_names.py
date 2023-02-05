## Solution #1

num = int(input())
people = set()

for person in range(num):
    name = input()
    people.add(name)

for person in people:
    print(person)

## Solution #2

# n = int(input())
# names_data = {input() for _ in range(n)}

# for name in names_data:
#     print(name)