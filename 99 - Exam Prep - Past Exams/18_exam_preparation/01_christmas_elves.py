from collections import deque

elves_input = deque([int(x) for x in input().split()])
material_boxes_input = deque([int(x) for x in input().split()])


def toy_maker(elves, material_boxes):
    toys = 0
    energy_used = 0
    counter = 0

    while True:

        if len(elves) == 0 or len(material_boxes) == 0:
            break
        elf = elves.popleft()
        counter +=1

        # checks if elf has energy lower than 5; if so just pops him out
        if elf < 5:
            counter -= 1
            continue
        # if he has energy more than 5 he will take the box
        else:
            current_material_box = material_boxes.pop()
        
        if (counter % 3 == 0 and counter % 5 == 0):
            energy_used += current_material_box * 2
            new_elf = elf-energy_used
            elves.append(new_elf)


        elif counter % 5 == 0:
            energy_used += current_material_box
            new_elf = elf-current_material_box
            elves.append(new_elf)


        elif counter % 3 == 0:
            current_material_box *= 2

            if elf >= current_material_box:
                toys += 2
                energy_used += current_material_box
                new_elf = elf-current_material_box + 1
                elves.append(new_elf)
    
            else:
                new_elf = 2*elf
                elves.append(new_elf)
                material_boxes.appendleft(current_material_box)
                
    
        # if it's not every third, fifth or a combined (e.g. 15th time)
        else:            
            if elf >= current_material_box:
                toys += 1
                energy_used += current_material_box 
                new_elf = elf - current_material_box + 1
    
            else:
                new_elf = 2*elf
                elves.append(new_elf)
                material_boxes.appendleft(current_material_box)
    
    

        
    return toys, energy_used, elves, material_boxes


print(toy_maker(elves_input,material_boxes_input))

