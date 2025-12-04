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


# ========================================
# Tuple, List
# ========================================
# 7.1
years_list = [1988, 1989, 1990, 1991, 1992, 1992]

# 7.2
# 1991

# 7.3
# 1992

# 7.4
things = ['mozzarella', 'cinderella', 'salmonella']

# 7.5
print(things[1].capitalize())

# 7.6
print(things[0].upper())

# 7.7
things.remove('salmonella')

# 7.8
surprise = ['Groucho', 'Chico', 'Harpo']

# 7.9
print(surprise[-1].lower()[::-1].capitalize())

# 7.10
even = [number for number in range(10) if number % 2 == 0]
print(even)

# 7.11
start1 = ['fee', 'fie', 'foe']
rhymes = [
    ('flop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call the judge'),
    ('fat', 'pet the cat'),
    ('fog', 'walk the dog'),
    ('fun', "say we're done"),
]
start2 = 'Someone better'

for first, second in rhymes:
    print(f'{" ".join([word.capitalize() for word in start1])}! {first.capitalize()}!')
    print(f'{start2} {second}.')


# ========================================
# Dictionary
# ========================================
# 8.1
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse',
}

# 8.2
print(e2f['walrus'])

# 8.3
f2e = {value: key for key, value in e2f.items()}

# 8.4
print(f2e['chien'])

# 8.5
print(set(f2e.keys()))

# 8.6
life = {
    'animals': {
        'cats': [
            'Henry',
            'Grumpy',
            'Lucy',
        ],
        'octopi': {},
        'emus': {},
    },
    'plants': {},
    'other': {},
}

# 8.7
print(life.keys())

# 8.8
print(life['animals'].keys())

# 8.9
print(life['animals']['cats'])

# 8.10
squares = {num: num**2 for num in range(10)}
print(squares)

# 8.11
odd = {num for num in range(10) if num % 2 == 0}
print(odd)

# 8.12
string_gen = (f'Got {num}' for num in range(10))
for text in string_gen:
    print(text)

# 8.13
person_types = (
    'optimist',
    'pessimist',
    'troll',
)
minds = (
    'The glass is half full',
    'The glass is half empty',
    'How did you get a glass?',
)

persons_dict = dict(
    zip(
        person_types,
        minds,
    ),
)

print(persons_dict)

# 8.14
titles = [
    'Creature of Habit',
    'Crewel Fate',
    'Sharks On a Plane',
]
plots = [
    'A nun turns into a monster',
    'A haunted yarn shop',
    'Check your exits',
]

movies = dict(zip(titles, plots))

print(movies)


# ========================================
# Functions
# ========================================
# 9.1
def good() -> list[str]:
    return ['Harry', 'Ron', 'Hermione']


# 9.2
def get_odds() -> list[int]:
    for index in range(10):
        if index % 2 != 0:
            yield index


for index, odd in enumerate(get_odds()):
    if index == 2:
        print(odd)


# 9.3
def test(func) -> None:
    def wrapper(*args, **kwargs) -> None:
        print('start')
        func(*args, **kwargs)
        print('end')

    return wrapper


@test
def hello() -> None:
    print('hello')


hello()


# 9.4
class OopsException(Exception):
    pass


def oops() -> None:
    raise OopsException


try:
    oops()
except OopsException:
    print('Caught an OopsException')


# ========================================
# Classes
# ========================================
# 10.1
class Thing:
    pass


print(Thing)

example = Thing()

print(example)


# 10.2
class Thing2:
    letters = 'abc'


print(Thing2.letters)


# 10.3
class Thing3:
    def __init__(self, letters):
        self.letters = letters


print(Thing3('xyz').letters)


# 10.4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'{self.name} {self.symbol} {self.number}'


element = Element('Hydrogen', 'H', 1)
print(f'{element.name} {element.symbol} {element.number}')

# 10.5
hydrogen_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(**hydrogen_dict)
print(f'{hydrogen.name} {hydrogen.symbol} {hydrogen.number}')

# 10.6
Element.dump = lambda self: print(f'({self.name}, {self.symbol}, {self.number})')
hydrogen.dump()

# 10.7
print(hydrogen)


# 10.8
class NewElement:
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number

    def __str__(self):
        return f'{self._name} {self._symbol} {self._number}'

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def number(self):
        return self._number


new_el = NewElement('Hydrogen', 'H', 1)
print(f'{new_el.name} {new_el.symbol} {new_el.number}')


# 10.9
class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


for animal in Bear(), Rabbit(), Octothorpe():
    print(f'{animal.__class__.__name__} eats: {animal.eats()}')


# 10.10
class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self, laser, claw, smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone

    def does(self):
        for part in self.laser, self.claw, self.smartphone:
            print(f'{part.__class__.__name__}: {part.does()}')


robot = Robot(Laser(), Claw(), SmartPhone())
robot.does()


# ========================================
# Modules
# ========================================
# 11.1
# 11.2
# 11.3
# 11.4
def get_hours():
    import zoo as menagerie

    menagerie.hours()


get_hours()


# 11.5
def get_plains():
    from zoo import plain

    print(plain)


get_plains()


# 11.6
def print_ordereddict() -> None:
    from collections import OrderedDict

    from zoo import plain

    od = OrderedDict(**plain)

    print(od)


print_ordereddict()


# 11.7
def print_ordereddict() -> None:
    from collections import defaultdict

    dict_of_lists = defaultdict(list)

    dict_of_lists['a'].append('something for a')

    print(dict_of_lists)


print_ordereddict()
