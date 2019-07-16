import time
#WHile loops

#syntax
# while <condition>:
#    code
#   **optional** if <condition>:
#                   break

counter = 0
while counter < 28:
    print('eat, sleep, rave!')
    counter += 1
    time.sleep(0.5)

print('ended loop')

while True:
    print('Welcome to the loop')
    word = input("Tell me a word")
    if word == 'bananas':
        print('you cracked the code')
        break
    else:
        print('haha you fool, you will never leave')