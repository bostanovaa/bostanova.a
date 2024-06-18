numbers = list(map(int, input("Введите набор целых чисел: ").split()))
start, end = map(int, input("Введите номер начала и конца: ").split())
product = 1
for i in range(start, end+1):
    product *= numbers[i]
print("Произведение чисел:", product)