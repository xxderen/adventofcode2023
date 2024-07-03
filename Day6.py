import re
import math
filename = "day6_input.txt"
with open(filename) as f:
    input = f.read()
def part1(input):
    possibility_list = []
    possibility = 0
    lines = input.split("\n")

    times = re.findall("\d+", lines[0])
    distances = re.findall("\d+", lines[1])
    for i in range(0,len(times)):
        for sec in range(0, int(times[i])):
            time = int(times[i])-sec
            total_distance = time * sec
            if total_distance > int(distances[i]):
                possibility += 1
        possibility_list.append(possibility)
        possibility = 0
    result = math.prod(possibility_list)
    return result

def part2(input):
    possibility_list = []
    possibility = 0
    lines = input.split("\n")
    times = re.findall("\d+", lines[0])
    times = times[0] + times[1] + times[2] + times[3] 
    distances = re.findall("\d+", lines[1])
    distances = distances[0] + distances[1] + distances[2] + distances[3] 
    for sec in range(0, int(times)):
            time = int(times)-sec
            total_distance = time * sec
            if total_distance > int(distances):
                possibility += 1
    possibility_list.append(possibility)
    possibility = 0
    result = math.prod(possibility_list)
    return result

print(part2(input))
