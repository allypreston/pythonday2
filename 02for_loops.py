import time
# for loops in python
# used to iterate over collections, lists and dictionaries

# syntax
# for <placeholder> in <list>:
    # run block of code

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

# list_data = [1, 2, 3, 4, 5]
# embedded_data = [[1,2,3],[5,6,7]]

# for num in list_data:
#     print(num)
#
# for data in embedded_data:
#     print(data)
#     for number in data:
#         print(number)

# for loops using dictionaries
# syntax is the same

# for <placeholder> in dictionary:
    # run block of code

# dict_data = {
#     'name': 'Bronson',
#     'money': 200
#}

# for key_placeholder in dict_data:
#     print(key_placeholder + ':',dict_data[key_placeholder])

embedded_dict_data = {
    1:{
        'name': 'Bronson',
        'money': 200
    },
    2:{
        'name': 'Tania',
        'money': 300
    },
    3:{
        'name': 'Tylor',
        'money': 400
    }
}
