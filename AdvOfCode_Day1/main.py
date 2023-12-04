import re

# "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
# re.findall("[0-9]", input[i])
# string_lst = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# re.findall(r"(?=("+'|'.join(string_lst)+r"))[0-9]", input[i])

nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
myFile = open("adventofcode_input.txt", "r")
data = myFile.read()
input = data.split("\n")
myFile.close()

coordinates = []

for i in range(len(input)):
    # This Find's and converts written out numbers
    wrtNums = re.findall(r"(?=(" + '|'.join(nums) + r"))", input[i])
    for x in wrtNums:
        digits = [nums[wrtNum] for wrtNum in wrtNums]

    # This is how I did Puzzle 1.1
    cI = re.findall("[0-9]", input[i])
    crd = int(cI[0] + cI[-1])
    coordinates.append(crd)

"""
print(input)
print(coordinates)
print("The total is:",sum(coordinates))
"""
