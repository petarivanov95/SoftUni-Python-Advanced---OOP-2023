healing_items = {'Patch': 30, 'Bandage':40, 'MedKit':100}
textiles = [int(x) for x in input().split()]
medicaments = [int(x) for x in input().split()]

created_items = {}


while textiles and medicaments:
    textile = textiles[0]
    medicament = medicaments[-1]
    total = textile + medicament
    
    if total in healing_items.values():
        for item, value in healing_items.items():
            if value == total:
                created_items[item] = created_items.get(item, 0) + 1
                textiles.pop(0)
                medicaments.pop()
                break
    elif total > healing_items['MedKit']:
        created_items['MedKit'] = created_items.get('MedKit', 0) + 1
        textiles.pop(0)
        medicaments.pop()
        remaining = total - healing_items['MedKit']
        next_medicament = medicaments.pop() + remaining
        medicaments.append(next_medicament)
    else:
        textiles.pop(0)
        new_medicament = medicaments.pop() + 10
        medicaments.append(new_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")
    
for item, amount in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
    print(f"{item} - {amount}")
    

if medicaments:
    print(f"Medicaments left: {', '.join(reversed(list(map(str,medicaments))))}")
if textiles:
    print(f"Textiles left: {', '.join((list(map(str,textiles))))}")
