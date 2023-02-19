jobs = [4, 10, 10, 6, 2, 99]
index = 2 

sorted_jobs = sorted(enumerate(jobs), key=lambda x: (x[1], x[0]))

print(sorted_jobs)