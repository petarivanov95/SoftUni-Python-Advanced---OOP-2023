from collections import deque

eggs_input = deque(int(x) for x in input().split(', '))
papers_input = deque(int(x) for x in input().split(', '))


def rotate_first_last_el(a_deck):
    front = a_deck.popleft()
    back = a_deck.pop()
    a_deck.append(front)
    a_deck.appendleft(back)

def wrapper(eggs, papers):
    box_count = 0
    box_size = 50

    while True:
        if len(eggs) > 0 and len(papers) > 0:
            egg = eggs.popleft()
            if egg == 13:   
                rotate_first_last_el(papers)
                continue
            elif egg <= 0:
                continue
            else:
                paper = papers.pop()
                if paper + egg <= box_size:
                    box_count += 1
                else:
                    continue
        else:
            break
    return box_count, eggs, papers

def main():
    boxes_total, eggs_final, papers_final = wrapper(eggs_input,papers_input)

    if boxes_total > 0:
        print(f"Great! You filled {boxes_total} boxes.")
    else:
        print("Sorry! You couldn't fill any boxes!")
    if len(eggs_final) > 0:
        eggs_str = ', '.join([str(x) for x in eggs_final])
        print(f'Eggs left: {eggs_str}')
    if len(papers_final) > 0:
        papers_str = ', '.join([str(x) for x in papers_final])
        print(f'Pieces of paper left: {papers_str}')
 
main()


# 20, 13, -7, 7
# 10, 5, 20, 15, 7, 9

# turn 1:
# 20 + 9 --> ok

# turn 2:
# 13 --> 
# -7, 7
# 7,5,20,15,10

# turn 3:
# -7 -->
# 7
# 7,5,20,15,10

# turn 4:
# 7,10 

# 2 boxes:
# 7,5,20,15

# Sample
# 20, 13, -7, 7
# 10, 5, 20, 15, 7, 9
# eggs = deque([20,13,-7,7])
# papers = deque([10,5,15,7,9])

# eggs = deque([2, 4, 7, 8, 0])
# papers = deque([5, 6, 2])


# while len(eggs) > 0 or len(papers) > 0:  
#     if len(eggs) and len(papers):
#         egg = eggs.popleft()
#         paper = papers.pop()


# print('eggs', eggs)
# print('papers', papers)