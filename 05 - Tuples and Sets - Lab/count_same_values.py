nums = tuple(map(float, input().split()))

values_counter = {value: nums.count(value) for value in nums}

for k,v in values_counter.items():
    print(f'{k} - {v} times')