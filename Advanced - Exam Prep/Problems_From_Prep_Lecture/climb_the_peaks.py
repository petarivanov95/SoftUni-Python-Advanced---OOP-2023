from collections import deque


def climb_the_peaks_func(food_portions, stamina):
    food_portions, stamina = deque(food_portions), deque(stamina)
    mountain_peaks_data = {'Vihren': 80, 'Kutelo':90, 'Banski Suhodol':100, 'Polezhan':60, 'Kamenitza':70}
    conquered_peaks = []
    failed_condition = False

    for peak_name, difficulty in mountain_peaks_data.items():
        while True:
            daily_sum_of_elements = food_portions.pop() + stamina.popleft()

            if daily_sum_of_elements >= difficulty:
                conquered_peaks.append(peak_name)
                break
            elif len(food_portions) == 0 or len(stamina) == 0:
                failed_condition = True
                break

        if failed_condition:
            if len(conquered_peaks) == 0:
                return 'Alex failed! He has to organize his journey better next time -> @PIRINWINS'
            else:
                data_representation = '\n'.join(conquered_peaks)
                return f'Alex failed! He has to organize his journey better next time -> @PIRINWINS\nConquered peaks:\n{data_representation}'

    data_representation = '\n'.join(conquered_peaks)
    return f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:\n{data_representation}'


food_input = [int(x) for x in input().split(', ')]
stamina_input = [int(x) for x in input().split(', ')]
print(climb_the_peaks_func(food_input, stamina_input))

#Sample Input
# 40, 40, 40, 40, 40, 40, 25
# 45, 50, 60, 20, 30, 5, 2
# For this input day 1 = 25+45 = 70 ---> not enough to climb Vihren (requires 80)
# For this input day 2 = 40+50 = 90 ---> enough to climb Vihren!
# For this input day 3 = 40+60 = 100 ---> enough to climb Kutelo!
# For this input day 4 = 40+20 = 60 ---> not enough to climb Banski Suhodol (requires 100)
# For this input day 5 = 40+30 = 70 ---> not enough to climb Banski Suhodol (requires 100)
# For this input day 1 = 40+5 = 45 ---> not enough to climb Banski Suhodol (requires 100)
# For this input day 1 = 40+2 = 42 ---> not enough to climb Banski Suhodol (requires 100)


