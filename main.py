import random
import itertools


# start with 21 numbers
numbers = list(range(1, 22))
# randomize the numbers
random.shuffle(numbers)
for i in range(3):
    # split number into three groups of seven
    groups = [[],[],[]]
    for i in range(0, 21, 3):
        groups[0].append(numbers[i])
        groups[1].append(numbers[i + 1])
        groups[2].append(numbers[i + 2])
    tenth_number = groups[1][3]
    print(f'group1: {groups[0]}\ngroup2: {groups[1]}\ngroup3: {groups[2]}')
    while True:
        input_text = input('think of a number and select the group (number only: 1, 2, 3): ')
        try:
            selected_group = int(input_text)
            if selected_group not in [1, 2, 3]:
                print('you need to select 1, 2, or 3')
                continue
            else:
                break
        except:
            print('you need to select 1, 2, or 3')
            continue
    print('')
    # put selected group in th middle
    groups[1], groups[selected_group - 1] = groups[selected_group - 1], groups[1]
    numbers = list(itertools.chain(*groups))
print(f'you are thinking of {numbers[10]}')
