import numpy as np
import random
rnd = np.array([random.random() for i in range(10)])
print(rnd)
with open("rnd_num.txt", "w") as file:
    file.write(str(rnd))