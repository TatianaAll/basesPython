numbers = input("Renseigner une liste de chiffre séparé par une virgule : ")

list_number = numbers.split(",")

list_number_int = []
for number in list_number:
    number = int(number)
    list_number_int.append(number)

sum_result = 0
for int in list_number_int:
    sum_result += int

mean_result = round(sum_result/len(list_number_int))
print(mean_result)

number_superior_mean = []
for int in list_number_int:
    if int >= mean_result:
        number_superior_mean.append(int)

print(number_superior_mean)