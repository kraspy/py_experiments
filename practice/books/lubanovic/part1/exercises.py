# ========================================
# Variables
# ========================================
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

# ========================================
# String
# ========================================
# 5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

print(
    song.replace(' m', ' M'),
)

# 5.2
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?",
]
answers = [
    'An exploding sheep.',
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel.",
]

print(
    f'Q: {questions[0]}\nA: {answers[0]}',
    f'Q: {questions[1]}\nA: {answers[1]}',
    f'Q: {questions[2]}\nA: {answers[2]}',
    sep='\n',
)

# 5.3
text = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s."""
print(text % ('roast beef', 'ham', 'head', 'clam'))


# 5.4
letter = """
Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}%s less likely to have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""


# 5.5
salutation = 'Mr.'
name = 'John'
product = 'mouse'
verbed = 'bit'
room = 'bedroom'
animals = 'cats'
amount = '10$'
percent = '30'
spokesman = 'John'
job_title = 'Manager'

print(
    letter.format(
        salutation=salutation,
        name=name,
        product=product,
        verbed=verbed,
        room=room,
        animals=animals,
        amount=amount,
        percent=percent,
        spokesman=spokesman,
        job_title=job_title,
    )
)

# 5.6
NAMES = ('McDuckface', 'McPumpkinface', 'McShpitzface')

print('Duck: %s,  Pumpkin: %s, Shpitz: %s' % NAMES)

# 5.7
print('Duck: {},  Pumpkin: {}, Shpitz: {}'.format(*NAMES))

# 5.8
print(f'Duck: {NAMES[0]},  Pumpkin: {NAMES[1]}, Shpitz: {NAMES[2]}')

# ========================================
# Loops
# ========================================
# 6.1
for i in [3, 2, 1, 0]:
    print(i)

# 6.2
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    number += 1

# 6.3
guess_me = 5

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
