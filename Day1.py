import re
#Test
filename = "day1_input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def part1():
    total = 0
    for line in input:
        line = re.sub('\D', '', line)       
        nums = int(line[0] + line[-1])      
        total += nums                 
    return total

def part2():
    values = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
        }
    pairs = []
    for line in input:
        digits = []
        for i,c in enumerate(line):
            if line[i].isdigit():
                digits.append(line[i])
            else:
                for k in values.keys():
                    if line[i:].startswith(k):
                        digits.append(values[k])
        pairs.append(int(str(digits[0])+str(digits[-1])))
    
    return sum(pairs)

print("Part one:", part1())
print("Part two:", part2())