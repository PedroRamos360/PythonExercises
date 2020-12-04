# Kaprekar's Constant

KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):
    number_of_iterations = 0
    while n != KAPREKAR_CONSTANT:
        number_of_iterations += 1
        # Criação e formatação dos números
        string_n = str(n)

        descending_list = sorted(string_n, reverse=True)
        ascending_list = sorted(string_n)

        descending_number = ""
        ascending_number = ""

        while len(descending_list) != 4:
            descending_list.append("0")

        for number in descending_list:
            descending_number += number
        for number in ascending_list:
            ascending_number += number

        # Cálculo da constante
        n = int(descending_number) - int(ascending_number)
        print("{} - {} = {}".format(int(descending_number), int(ascending_number), n))
    
    return number_of_iterations

print(num_kaprekar_iterations(1476))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)