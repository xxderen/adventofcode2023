filename = "day15_input.txt"
with open(filename) as f:
    input = f.read().split(",")
#Test
result = 0

def hash(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

for i in range(0,len(input)):
    result += hash(input[i])

print(result)
