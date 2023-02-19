from collections import deque


# get the names of the players as a space-separated string and split it into a list
name_of_players = input().split(' ')

# get the number of steps that the "hot potato" should be passed
step_of_hot_potato = int(input())

# create a double-ended queue from the list of player names
players_deque = deque(name_of_players)


# run the simulation until only one player remains
while len(players_deque) > 1:
    # pass the "hot potato" step_of_hot_potato-1 times by removing the first player and appending it to the end of the queue
    for _ in range(step_of_hot_potato - 1):
        players_deque.append(players_deque.popleft())

    # remove the player who has the "hot potato" and print their name
    print(f'Removed {players_deque.popleft()}')

# print the name of the last player remaining
print(f'Last is {players_deque.pop()}')

