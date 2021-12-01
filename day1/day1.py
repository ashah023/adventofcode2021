lines=[]
with open('input.txt') as f:
    lines=f.readlines()

depths=map(lambda x: x.to_i, lines)

# Part 1
count=0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        count += 1

print(count)

# Part 2
windows=[]
for i in range(0, len(depths)-2):
  windows.append(depths[i]+depths[i+1]+depths[i+2])

count=0
for i in range(1, len(windows)):
  if windows[i] > windows[i-1]:
    count+=1

print(count)