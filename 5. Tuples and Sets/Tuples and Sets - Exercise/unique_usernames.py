num = int(input())

unique_names = set()

for _ in range(num):
    one_name = input()
    unique_names.add(one_name)

for name in unique_names:
    print(name)