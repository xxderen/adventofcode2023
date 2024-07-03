import re
import math
filename = "day2_input.txt"
input = []
with open(filename) as f:
    input = f.read()

def part1(input):
    possible = {"red": "12", "green": "13", "blue": "14"}
    result = 0
    for id, game in enumerate(input.split("\n"), start=1):

        for number, color in re.findall(r"(\d+) (red|green|blue)", game):
            if int(possible[color]) < int(number):
                break
        else:
            result += id

    return result

def part2(input):
    result = 0
    for game in input.split("\n"):
        max_number = {"red": 0, "green": 0, "blue": 0}

        for number, color in re.findall(r"(\d+) (red|green|blue)", game):
            max_number[color] = max(max_number[color], int(number))

        result += math.prod(max_number.values())

    return result

print(part1(input))
print(part2(input))

