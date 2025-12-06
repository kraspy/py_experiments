import os

# 14.1
current_dir = os.path.dirname(__file__)
print(os.listdir(current_dir))

# 14.2
parent_dir = os.path.split(current_dir)[0]
print(os.listdir(parent_dir))

# 14.3
test1 = 'This is a test of the emergency text system'

with open('test.txt', 'w') as f:
    f.write(test1)

# 14.4
with open('test.txt', 'r') as f:
    test2 = f.read()

print(test2 == test1)
