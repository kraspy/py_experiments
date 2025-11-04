numbers = []
powerball_numbers = []

with open('pbnumbers.txt') as f:
    while line := f.readline():
        *nums, pb_num = line.strip().split(' ')
        numbers.extend(nums)
        powerball_numbers.append(pb_num)

numbers.sort()
powerball_numbers.sort()

tmp_num = []
tmp_num_frequency = []

tmp_pb = []
tmp_pb_frequency = []

for num in numbers:
    if num not in tmp_num:
        tmp_num.append(num)
        tmp_num_frequency.append(1)
    else:
        tmp_num_index = tmp_num.index(num)
        tmp_num_frequency[tmp_num_index] += 1

for pb_num in powerball_numbers:
    if pb_num not in tmp_pb:
        tmp_pb.append(pb_num)
        tmp_pb_frequency.append(1)
    else:
        tmp_pb_num_index = tmp_pb.index(pb_num)
        tmp_pb_frequency[tmp_pb_num_index] += 1

nums_with_frequency = sorted(
    list(zip(tmp_num, tmp_num_frequency)),
    key=lambda x: x[1],
    reverse=True,
)
pb_nums_with_frequency = sorted(
    list(zip(tmp_pb, tmp_pb_frequency)),
    key=lambda x: x[1],
    reverse=True,
)

print('10 наиболее распростаненных чисел, упорядоченных по частоте: ')
for pair in nums_with_frequency[:10]:
    print(f'Число "{pair[0]}": Встречается {pair[1]} раз')
print('\n')

print('10 наиболее распростаненных Powerball-чисел, упорядоченных по частоте: ')
for pair in pb_nums_with_frequency[:10]:
    print(f'PowerBall-число "{pair[0]}": Встречается {pair[1]} раз')
print('\n\n')

print('Частота каждого числа: ')
for pair in sorted(nums_with_frequency):
    print(f'"{pair[0]}": {pair[1]} раз')
print('\n')

print('Частота каждого Powerball-числа: ')
for pair in sorted(pb_nums_with_frequency):
    print(f'PowerBall-число "{pair[0]}": {pair[1]} раз')
print('\n\n')
