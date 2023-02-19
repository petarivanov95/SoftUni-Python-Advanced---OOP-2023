from collections import deque

healing_items = {'Patch': 30, 'Bandage':40, 'MedKit':100}
textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

created_items = {}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    total = textile + medicament
    
    if total in healing_items.values():
        for item, value in healing_items.items():
            if value == total:
                created_items[item] = created_items.get(item, 0) + 1
    elif total > healing_items['MedKit']:
        created_items['MedKit'] = created_items.get('MedKit', 0) + 1
        remaining = total - healing_items['MedKit']
        next_medicament = medicaments.pop() + remaining
        medicaments.append(next_medicament)
    else:
        new_medicament = medicament + 10
        medicaments.append(new_medicament)

if (not textiles) and (not medicaments):
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

if created_items:
    sorted_dict = sorted(created_items.items(), key=lambda x: (-x[1],x[0]))
    for item, amount in sorted_dict:
        print(f"{item} - {amount}")
        
if medicaments:
    print(f"Medicaments left: {', '.join(map(str, sorted(medicaments,reverse=True)))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, sorted(textiles,reverse=True)))}")
