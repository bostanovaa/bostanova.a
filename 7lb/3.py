import math
import random

for _ in range(10):
    num = random.randint(-10, 10)
    if num == 0:
        break
    elif num < 0:
        continue
    else:
        print(math.sqrt(num))