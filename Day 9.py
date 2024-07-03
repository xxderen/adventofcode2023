with open('9.in') as f:
    lines = f.read().splitlines()

lines = [[int(i) for i in line.split()] for line in lines]

r1 = 0
r2 = 0

# Iterate over each line in the input
for line in lines:
    h = [line]

    # Calculate differences until all elements in the last list are 0
    while any([h[-1][i] != 0 for i in range(len(h[-1]))]):
        # Calculate the differences between consecutive elements in the previous list
        h.append([h[-1][i+1] - h[-1][i] for i in range(len(h[-1]) - 1)])

    # Sum the last elements of each list in 'h' for r1
    r1 += sum([h[i][-1] for i in range(len(h))])

    # Calculate the weighted sum of the first elements of each list in 'h' for r2
    r2 += sum([h[i][0] * (1 - 2*(i%2)) for i in range(len(h))])

print(r1)
print(r2)