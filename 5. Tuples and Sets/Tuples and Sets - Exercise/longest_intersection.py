import sys 

max_len = -1*sys.maxsize

num_lines = int(input())
dict_of_intersections = {}

for x in range(num_lines):
    incoming_string = [list(map(int, x.split(','))) for x in input().split('-')]
    set_1 = set(range(incoming_string[0][0],incoming_string[0][1]+1))
    set_2 = set(range(incoming_string[1][0],incoming_string[1][1]+1))
    intersection = set_1.intersection(set_2)
    dict_of_intersections[x] = [intersection, len(intersection)]


for k,v in dict_of_intersections.items():

    if v[1] > max_len:
        max_len = v[1]
        list_needed = [k,v]

print(f"Longest intersection is {sorted(list(dict_of_intersections[list_needed[0]][0]))} with length {max_len}")
# print(dict_of_intersections)