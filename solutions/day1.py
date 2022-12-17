file = open("../puzzle_input/day1.txt","r")
most_calorie = []
current = 0
while True:
  input = file.readline()
  if not input:
    break;
  if input == "\n":
    if(len(most_calorie) < 3):
      most_calorie.insert(0,current)
    else:
      if(current > min(most_calorie)):
        most_calorie.remove(min(most_calorie))
        most_calorie.insert(0,current)
    current = 0
  else:
    current += int(input)
file.close()

print("Most calorie an elf hold:",max(most_calorie))
print("Sum of the calorie the top 3 elves hold:",sum(most_calorie))
