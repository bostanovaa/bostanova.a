n = int(input("Введите количество специальностей: "))
specialties = {}
for i in range(n):
    specialty_info = input("Введите название специальности и номера групп через тире: ").split('-')
    specialty_name = specialty_info[0]
    groups = specialty_info[1].split(',')
    for group in groups:
        specialties[group.strip()] = specialty_name
group_number = input("Введите номер группы: ")
print("Название специальности:", specialties.get(group_number, ""))