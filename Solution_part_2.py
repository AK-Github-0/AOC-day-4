f = open("input.txt", "r")
answer = []
counter = 0
for line in f:
    a = line.split("\n")[0]
    a, b = line.split(",")[0], line.split(",")[1]
    a1, a2 = a.split("-")[0], a.split("-")[1]
    b1, b2 = b.split("-")[0], b.split("-")[1]
    temp1 = [i for i in range(int(a1), int(a2)+1)]
    temp2 = [i for i in range(int(b1), int(b2)+1)]
    if(any(x in temp1 for x in temp2) or any(x in temp2 for x in temp1)):
      counter += 1
counter
