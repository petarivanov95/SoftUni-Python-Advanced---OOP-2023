from collections import deque

tasks = deque([int(x) for x in input().split(', ')])
selected_index = int(input())

def sjf(jobs, index):
    # Sort the list of jobs by their clock-cycles in ascending order,
    # with ties broken by their original order in the list (FIFO)
    sorted_jobs = sorted(enumerate(jobs), key=lambda x: (x[1], x[0]))
    
    # Start with a time of 0
    time = 0
    
    # Iterate through the sorted list of jobs
    for i, job in sorted_jobs:
        # If we've reached the job we're interested in, return the time it will be completed
        if i == index:
            return time + job
        # Otherwise, add the current job's clock-cycles to the total time
        time += job

print(sjf(tasks,selected_index))


