x_crazy_landlords = ['Cruella de Ville', 'Donald Duck', 'Popeye the Maltese']
counter = 1
print('loop started')
for landlord in x_crazy_landlords:
    print(counter, '-', landlord)
    counter += 1
print('loop ended')

spartans = [['shav', 'adam', 'julian', 'muji', 'ally'], ['pratheep', 'zaid', 'omid', 'payal', 'micheal']]
counter = 1
for team in spartans:
    for name in team:
        print('hello', name, 'you are on team', counter)
    counter += 1

