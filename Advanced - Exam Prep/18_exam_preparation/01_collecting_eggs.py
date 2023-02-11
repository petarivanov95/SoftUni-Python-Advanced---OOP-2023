from collections import deque

# Define the input for eggs and papers as deques, with each element being an integer.
eggs_input = deque(int(x) for x in input().split(', '))
papers_input = deque(int(x) for x in input().split(', '))

# Function to rotate the first and last element of a deck.
def rotate_first_last_el(a_deque):
    front = a_deque.popleft()   # Pop the first element from the deque.
    back = a_deque.pop()        # Pop the last element from the deque.
    a_deque.append(front)       # Append the popped first element to the end of the deque.
    a_deque.appendleft(back)    # Append the popped last element to the beginning of the deque.

# Function to fill boxes with eggs and papers.
def wrapper(eggs, papers):
    box_count = 0         # Counter to keep track of the number of boxes filled.
    box_size = 50         # The size of each box.

    # Continuously loop until there are no more eggs or papers left.
    while True:
        # Check if there are still eggs and papers left.
        if len(eggs) > 0 and len(papers) > 0:
            egg = eggs.popleft()   # Pop the first egg from the deck.
            if egg == 13:
                # If the egg size is 13, rotate the papers deck.
                rotate_first_last_el(papers)
                continue
            elif egg <= 0:
                # If the egg size is less than or equal to 0, skip it.
                continue
            else:
                paper = papers.pop()     # Pop the last piece of paper from the deck.
                if paper + egg <= box_size:
                    # If the egg and paper combined size is less than or equal to the box size, fill a box.
                    box_count += 1
                else:
                    continue
        else:
            # If there are no more eggs or papers, break out of the loop.
            break
    return box_count, eggs, papers

def main():
    # Call the wrapper function to fill boxes with eggs and papers.
    boxes_total, eggs_final, papers_final = wrapper(eggs_input,papers_input)

    # Check if any boxes were filled and print the result.
    if boxes_total > 0:
        print(f"Great! You filled {boxes_total} boxes.")
    else:
        print("Sorry! You couldn't fill any boxes!")
    # Check if there are any eggs left and print the result.
    if len(eggs_final) > 0:
        eggs_str = ', '.join([str(x) for x in eggs_final])
        print(f'Eggs left: {eggs_str}')
    # Check if there are any pieces of paper left and print the result.
    if len(papers_final) > 0:
        papers_str = ', '.join([str(x) for x in papers_final])
        print(f'Pieces of paper left: {papers_str}')

# Call the main function.
main()
