num_lines = int(input())
set_compounds = set()

for _ in range(num_lines):
    entry = input().split()
    set_compounds.update(entry)

for compound in set_compounds:
    print(compound)