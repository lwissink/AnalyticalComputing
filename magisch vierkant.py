from time import sleep

magic = []
magic.append([8, 0, 0])
magic.append([0, 5, 0])
magic.append([0, 7, 0])

total = 15

def checkGrid(magic):
    global total
    for row in range(0, 3):
        for col in range(0, 3):
            if magic[row][col] == 0:
                return False
    for row in range(0, 3):
        if (magic[row][0] + magic[row][1] + magic[row][2]) != total:
            return False
    for col in range(0, 3):
        if (magic[0][col] + magic[1][col] + magic[2][col]) != total:
            return False
    if (magic[0][0] + magic[1][1] + magic[2][2]) != total:
        return False
    if (magic[0][2] + magic[1][1] + magic[2][0]) != total:
        return False
    return True

def solveGrid(magic):
    for i in range(0, 9):
        row = i // 3
        collum = i % 3
        if magic[row][collum] == 0:
            for value in range(1, 10):
                if not (value in magic[0] or value in magic[1] or value in magic[2]):
                    magic[row][collum] = value
                    if checkGrid(magic):
                        return True
                    else:
                        if solveGrid(magic):
                            return True
            break
    magic[row][collum] = 0

sleep(1)

solved = solveGrid(magic)
if solved:
    print(magic[0])
    print(magic[1])
    print(magic[2])
else:
    print("kan niet")
