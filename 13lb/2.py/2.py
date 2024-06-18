numbers = list(map(int, input("Введите набор целых чисел, разделённых пробелами: ").split()))
start, end = map(int, input("Введите два целых числа X и Y: ").split())
if start < 0 or end >= len(numbers) or start > end:
    print("Некорректные номера, попробуйте еще раз")
else:
    total = sum(numbers[start:end+1])
    print("Сумма чисел от номера", start, "до номера", end, "равна:", total)