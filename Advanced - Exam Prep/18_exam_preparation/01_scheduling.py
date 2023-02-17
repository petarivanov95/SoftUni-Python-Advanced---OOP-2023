from collections import deque

tasks = deque([int(x) for x in input().split(', ')])
selected_index = int(input())

def sjf(jobs, index):
    # Sort the list of jobs by their clock-cycles in ascending order,
    # with those with equal result broken by their original order in the list (FIFO)
    # ---
    # enumerate takes the original index and job, this will be used to then sort them
    # by x[1], which is the job size and if the sizes are the same at x[1] then x[0]
    # will be used, which in turn will rank them based on the index from the original list
    # to adhere to the FIFO order requirement
    
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


