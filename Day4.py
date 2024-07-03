import re
#Test
filename = "day4_input.txt"
with open(filename) as f:
    input = f.read()
def part1(input):
    number = 0
    total = 0

    for line in input.split("\n"):
        winners, nums = line.split("|")
        ours = nums.split()
        wins = winners.split()
        wins.pop(0)
        wins.pop(0)
        for our in ours:
            if our in wins:
                number += 1
        
        if number == 1:
            total += 1

        elif number == 2:
            total += 2

        elif number == 3:
            total += 4

        elif number == 4:
            total += 8

        elif number == 5:
            total += 16

        elif number == 6:
            total += 32

        elif number == 7:
            total += 64

        elif number == 8:
            total += 128

        elif number == 9:
            total += 256

        elif number == 10:
            total += 512
        number = 0

    return total

def part2(input):
    lines = input.split("\n")
    regex = r":(.*)\|(.*)"
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        win_nums, actual_nums = re.findall(regex, line)[0]
        overlap = set(win_nums.split()) & set(actual_nums.split())
        for j in range(len(overlap)):
            cards[i+j+1] += cards[i]
    
    return sum(cards)

print(part1(input))
print(part2(input))

