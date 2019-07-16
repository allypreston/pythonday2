import time
# for loops in python
# used to iterate over collections, lists and dictionaries

# syntax
# for <placeholder> in <list>:
    # run block of cold

# x_crazy_landlords = ['Cruella de Ville', 'Donald Duck', 'Popeye the Maltese']
# counter = 0
# print('starting loop')
# for landlord in x_crazy_landlords:
#     print('hello ' + landlord)
#     print(counter)
#     counter += 1
#     time.sleep(1)
# print('loop ended')

#further loops

list_data = [1, 2, 3, 4, 5]
embedded_data = [[1,2,3],[5,6,7]]

# for num in list_data:
#     print(num)

for data in embedded_data:
    print(data)
    for number in data:
        print(number)