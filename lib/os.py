import copy

queue = [143, 86, 1470, 913, 1774, 948, 1509, 1022, 1750, 130]

# Using FCFS
prev = None

total = 0

for i in queue:
    if prev is not None:
        total += abs(i-prev)
        prev = i
    else:
        prev = i
print "a. FCFS:", total