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

weather = input('What is the weather like? ').lower().strip()

if weather == 'sunny':
    print('You should probably take a sunhat.')
elif weather == 'rainy' or weather == 'stormy':
    print('You should bring an umbrella then.')
else:
    print('Better take both an umbrella and a sunhat, just to be safe.')