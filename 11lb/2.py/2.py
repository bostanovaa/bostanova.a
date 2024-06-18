B = []
for i in range(20):
    num = float(input("Введите элемент списка B: "))
    B.append(num)
sum_positive = sum(num for num in B if num > 0)
print("Сумма положительных элементов списка B:", sum_positive)
