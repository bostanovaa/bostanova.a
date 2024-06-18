A = [] 
import random
for _ in range(20):
    A.append(random.randint(-10, 10))
print("Список A:", A)
negative = len([x for x in A if x < 0])
print("Количество отрицательных элементов списка A:", negative)