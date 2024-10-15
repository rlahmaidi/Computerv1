import re
from math import sqrt, fabs
import sys


def Reduced(equ_coef):
    if all(x == 0 for x in equ_coef):
        print("Reduced form: 0 * X^0 = 0")
    else:
        i = 0
        text = ""
        for i in range(len(equ_coef)):
            if equ_coef[i] != 0:
                if equ_coef[i] < 0:
                    text += ' - '
                elif equ_coef[i] > 0 and i != 0 and text != "":
                    text += ' + '
                # if isinstance(equ_coef[i], int):
                #     text += str(abs(equ_coef[i]))
                # elif isinstance(equ_coef[i], float):
                #     text += str(fabs(equ_coef[i]))
                if equ_coef[i] < 0:
                    text += str((-1) * equ_coef[i])
                else:
                    text += str(equ_coef[i])
                text += " * X^" + str(i)
        text += " = 0"
        print("Reduced form: ", text)


def is_float(coef):
    import re

    coef = coef.replace(" ", "")
    pattern = r"[^0-9.]"

    match = re.search(pattern, coef)

    if match:
        print("coefficient should be integers or floats only")
        sys.exit()
    else:
        pattern = r"[.]"
        if re.search(pattern, coef):
            return True
        else:
            return False


def one_part_coef(part):
    minus_taken_from_beg = part
    if part[0] == '-':
        minus_taken_from_beg = part[1:]
    split_by_sign = re.split('[+-]', minus_taken_from_beg)
    coef = []
    for element in split_by_sign:
        split_by_etoile = element.split('*')
        if is_float(split_by_etoile[0]):
            coef.append(float(split_by_etoile[0]))
        else:
            coef.append(int(split_by_etoile[0]))
    # looking for minus and plus
    index = 0
    dic = {}
    # looking for minus
    while index < len(part):
        index = part.find('-', index)
        if index == -1:
            break
        dic[index] = -1
        index += 1
    # looking for +
    index = 0
    while index < len(part):
        index = part.find('+', index)
        if index == -1:
            break
        dic[index] = 1
        index += 1
    if len(dic) < len(split_by_sign):
        dic[0] = 1
    # sort the dic
    myKeys = list(dic.keys())
    myKeys.sort()
    sorted_dict = {i: dic[i] for i in myKeys}
    # multiply coef by their signs
    i = 0
    for key, value in sorted_dict.items():
        coef[i] = coef[i] * value
        i += 1
    while len(coef) < 3:
        coef.append(0)
    return coef


def polynom_coefficient(left_coef, right_coef):
    while len(left_coef) < len(right_coef):
        left_coef.append(0)
    while len(right_coef) < len(left_coef):
        right_coef.append(0)
    equ_coef = []
    for i in range(len(right_coef)):
        equ_coef.append(left_coef[i] + right_coef[i])
    return equ_coef

def equation_degree(equ_coef):
    #for the special case a * X^0 = a * X^0
    if all(x == 0 for x in equ_coef):
        return 0
    tmp_list = equ_coef[::-1]
    deg = len(equ_coef) - 1
    for el in tmp_list:
        if el != 0:
            break
        else:
            deg = deg - 1
    return deg



if __name__ == "__main__":
    equation = input("give me an equation to solve: ")
    #trimmed to get rid of double quotes
    equation = equation[1:-1]
    equ_spl_by_equal = equation.split("=")
    left_coef = one_part_coef(equ_spl_by_equal[0])
    right_coef = one_part_coef(equ_spl_by_equal[1])
    right_coef = [i * (-1) for i in right_coef]
    equ_coef = polynom_coefficient(left_coef, right_coef)
    Reduced(equ_coef)
    degree = equation_degree(equ_coef)
    print("Polynomial degree:", degree)
    # solving the equation
    if degree > 2:
        print("The polynomial degree is strictly "
              "greater than 2, I can't solve.")
    elif degree == 0:
        if equ_coef[0] == 0:
            print("every real number is a solution")
        else:
            print("there is no solution to this equation")
    elif degree == 1:
        print("the solution of this equation is: ")
        print((-1) * equ_coef[0] / equ_coef[1])
    else:
        delta = equ_coef[1]**2 - 4 * equ_coef[0] * equ_coef[2]
        print("delta is ", delta)
        if delta < 0:
            print("Discriminant is strictly negative, i can't solve this")
        elif delta == 0:
            print("Discriminant is null, the solution is:")
            sol = (-1) * equ_coef[1]/(2 * equ_coef[2])
            print(sol)
        else:
            print("Discriminant is strictly positive ,the two solutions are:")
            sol1 = ((-1) * equ_coef[1] - delta**(1/2)) / (2 * equ_coef[2])
            sol2 = ((-1) * equ_coef[1] + delta**(1/2))/ (2 * equ_coef[2])
            print(sol1)
            print(sol2)
