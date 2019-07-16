# control flow - if statements
# if statements use logical comparitors

#if <condition>:
    #block of code
#elif <condition>:
    #block of code
#else:
    #block of code

# age = 16
#
# if age >= 18:
#     print('your age is above 18')
# elif age >= 16:
#     print('you are under age to vote, but you can buy lottery tickets')
# else:
#     print('you are a child, stay in school')

# weather = input('What is the weather like? ').lower().strip()
#
# if weather == 'sunny':
#     print('You should probably take a sunhat.')
# elif weather == 'rainy' or weather == 'stormy':
#     print('You should bring an umbrella then.')
# else:
#     print('Better take both an umbrella and a sunhat, just to be safe.')

#I want a jacket when it is rainy and stormy
#I want an umbrella only when it is rainy
#I want a umbrella  if it is foggy
#keep stuff from sunny

# weather1 = input('what is the weather like?').lower().strip()
# weather2 = input('what is the weather like?').lower().strip()
#
# if (weather1 == 'stormy' and weather2 == 'rainy') or (weather2 == 'stormy' and weather1 == 'rainy'):
#     print('Take your jacket.')
# elif (weather1 == 'rainy' or weather2 == 'foggy') or (weather2 == 'rainy' or weather1 == 'foggy'):
#     print('Take your umbrella')
# elif weather1 == 'sunny' or weather2 == 'sunny':
#     print('Take sunglasses')
# else:
#     print('live your best life')

weather = input('what is the weather like? ').lower().strip()
if 'stormy' in weather and 'rainy' in weather:
    print('take an jacket')
elif 'rainy' in weather or 'foggy' in weather:
    print('take an umbrella')
elif 'sunny' in weather:
    print('take your sunglasses')
else:
    print('live your best life')