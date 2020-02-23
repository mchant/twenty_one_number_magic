import random
import itertools


# start with 21 numbers
numbers = list(range(1, 22))
# randomize the numbers
random.shuffle(numbers)
for i in range(3):
    # split number into three groups of seven
    groups = [[numbers[i + j] for i in range(0, 21, 3)] for j in range(3)]
    print(f'group1: {groups[0]}\ngroup2: {groups[1]}\ngroup3: {groups[2]}')
    while True:
        input_text = input('think of a number and select the group (number only: 1, 2, 3): ')
        if input_text not in ['1', '2', '3']:
            print('you need to pick 1, 2, or 3')
            continue
        else:
            selected_group = int(input_text)
            break
    print('\n')
    # put selected group in th middle
    groups[1], groups[selected_group - 1] = groups[selected_group - 1], groups[1]
    # flatten the list and keep going
    numbers = list(itertools.chain(*groups))
print(f'you are thinking of {numbers[10]}')
