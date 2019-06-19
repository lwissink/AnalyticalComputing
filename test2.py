import numpy as np
import json

o1 = 0
o2 = 0
o3 = 0
o4 = 0

with open('example.json') as json_file:
    data = json.load(json_file)


input = np.array([1,
              1,
              1,
              1,
              1])


print(input)

weights = data["layer1"]["weights"]



for i in weights:
    j = str(i)
    for x, y in weights[j].items():
        x = int(x)
        y = float(y)
        if x == 1:
            o1 = o1 + (y * input[x-1])
        if x == 2:
            o2 = o2 + (y * input[x-1])
        if x == 3:
            o3 = o3 + (y * input[x-1])
        if x == 4:
            o4 = o4 + (y * input[x-1])

output = np.array([o1,
                   o2,
                   o3,
                   o4])
print(output)

