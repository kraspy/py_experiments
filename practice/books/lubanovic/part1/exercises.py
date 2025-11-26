# 4.1

secret = 5
guess = 3

if guess < 7:
    print('too low')
elif guess > 7:
    print('too high')
elif guess == secret:
    print('just right')

# 4.2
small = True
green = False

if small and not green:
    print('cherry')
elif small and green:
    print('pea')
elif not small and not green:
    print('watermelon')
elif not small and green:
    print('pumpkin')
