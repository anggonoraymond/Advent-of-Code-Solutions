# Puzzle #1 
file = open("day2.txt","r")
puzzle1_points = 0
shape_points = {"X":1,"Y":2,"Z":3}
rule ={"A":{"Y":6,"X":3},"B":{"Z":6,"Y":3},"C":{"X":6,"Z":3}}
while True:
  line = file.readline()
  if not line:
    break;
  input = line.replace('\n','').split(' ')
  puzzle1_points += shape_points[input[1]]
  if(input[1] in rule[input[0]]):
    puzzle1_points+= rule[input[0]][input[1]]
file.close()
print(puzzle1_points)

# Puzzle #2
file = open("day2.txt","r")
puzzle2_points = 0
action_points = {"X":0,"Y":3,"Z":6}
shape_points = {"X":1,"Y":2,"Z":3}
rule ={"A":{0:shape_points["Z"],3:shape_points["X"],6:shape_points["Y"]},"B":{0:shape_points["X"],3:shape_points["Y"],6:shape_points["Z"]},"C":{0:shape_points["Y"],3:shape_points["Z"],6:shape_points["X"]}}
while True:
  line = file.readline()
  if not line:
    break;
  input = line.replace('\n','').split(' ')
  puzzle2_points += action_points[input[1]]
  puzzle2_points +=rule[input[0]][action_points[input[1]]]
file.close()
print(puzzle2_points)
