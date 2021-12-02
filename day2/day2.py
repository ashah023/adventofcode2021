with open('input.txt') as f:
    lines = f.readlines()

'''
# Part 1
horizontal_pos=0
vertical_pos=0
for line in lines:
    move, pos = line.split(' ')
    pos = int(pos)
    if move == 'forward':
        horizontal_pos += pos
    elif move == 'down':
        vertical_pos += pos
    else:
        vertical_pos -= pos

print(vertical_pos * horizontal_pos)
'''


# Part 2
horizontal_pos=0
vertical_pos=0
aim=0
for line in lines:
    move, pos = line.split(' ')
    pos = int(pos)
    if move == 'forward':
        horizontal_pos += pos
        vertical_pos += aim * pos
    elif move == 'down':
        aim += pos
    else:
        aim -= pos

print(vertical_pos * horizontal_pos)