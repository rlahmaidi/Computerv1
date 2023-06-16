import re
from math import sqrt, fabs
import sys
# To be done:
# 1 - display the reduced form of a degree> 2
# 2 - display the reduced form of a degree < 2

def Reduced(equ_coef):
    i = 0
    text = ""
    for i in range(len(equ_coef)):
        if equ_coef[i] != 0:
            if equ_coef[i] < 0:
                text += ' - '
            elif equ_coef[i] > 0 and i != 0:
                text += ' + '
            if isinstance(equ_coef[i], int):
                text += str(abs(equ_coef[i]))
            elif isinstance(equ_coef[i], float):
                text += str(fabs(equ_coef[i]))
            text += " * X^" + str(i)
    text += " = 0"
    print("Reduced form: ",text)
                

# def reduced_form(equ_coef):
#     sign1 ='+'
#     sign2 = '+'
#     text = "Reduced form: {} * X^0 {} {}  * X^1 {} {} * X^2 = 0"
#     if equ_coef[1] < 0:
#         sign1 = "-"
#     if equ_coef[2] < 0:
#         sign2 = '-'
#     print(text.format(equ_coef[0], sign1, fabs(equ_coef[1]), sign2, fabs(equ_coef[2],)))


def  one_part_coef(part):
    split_by_sign =  re.split('[+-]', part)
    # if len(split_by_sign) > 3:
    #     print("Polynomial degree: ", len(split_by_sign))
    #     print("The polynomial degree is strictly greater than 2, I can't solve.")
    #     sys.exit()
    coef = []
    for element in split_by_sign:
        split_by_etoile = element.split('*')
        # perhaps some function for error management here
        if split_by_etoile[0].isdigit() is True:
            coef.append(int(split_by_etoile[0]))
        else:
            try:
                coef.append(float(split_by_etoile[0]))
            except Exception:
                print("the polynomial coefficient should be integer or float")
                sys.exit()
    # print(coef)
    # looking for minus and plus

    index = 0
    dic = {}
    # looking for minus
    while index < len(part):
        index = part.find('-',index)
        if index == -1:
            break
        dic[index] = -1
        index += 1
    # looking for +
    index = 0
    while index < len(part):
        index = part.find('+',index)
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
    for key,value in sorted_dict.items():
        coef[i] = coef[i] * value
        i += 1
    while len(coef) < 3:
        coef.append(0)
    return coef



if __name__ == "__main__":
    equation = input("give me an equation to solve: ")
    equ_spl_by_equal = equation.split("=")
    left_coef = one_part_coef(equ_spl_by_equal[0])
    right_coef = one_part_coef(equ_spl_by_equal[1])
    right_coef = [i * (-1) for i in right_coef]
    # calculate the equation coefficient
    while len(left_coef) < len(right_coef):
        left_coef.append(0)
    while len(right_coef) < len(left_coef):
        right_coef.append(0)
    equ_coef = []
    for i in range(len(right_coef)):
        equ_coef.append(left_coef[i] + right_coef[i])
    # calculatin the equation degree
    equ_degre = -1
    for el in equ_coef:
        # the weird thing below need to be tested
        if el != 0.0:
            equ_degre += 1
    Reduced(equ_coef)
    print("Polynomial degree: ", equ_degre)
    # solving the equation
    if len(equ_coef) > 3 :
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    elif equ_coef[1] == equ_coef[2] == 0:
        if equ_coef[0] == 0:
            print("i.e every real number is a solution")
        else:
            print("the only solution for this equation is 0")
    elif equ_coef[2] == 0 and equ_coef[1] != 0:
        print("the solution of this equation is: ")
        print((-1) * equ_coef[0] / equ_coef[1])
    else:
        # reduced_form(equ_coef)
        delta = equ_coef[1]**2 - 4 * equ_coef[0] * equ_coef[2]
        if delta < 0:
            print("")
            print("i can't solve this")
        elif delta == 0:
            print("the solution is:")
            sol = (-1) * equ_coef[1]
        else:
            print("the solutions are:")
            sol1 = ((-1) * equ_coef[1] - sqrt(delta)) / (2 * equ_coef[2])
            sol2 = ((-1) * equ_coef[1] + sqrt(delta)) / (2 * equ_coef[2])

            print(sol1)
            print(sol2)


    # print("value of equ splitted by = is:")
    # print(equ_spl_by_equal)
    # print("the left coef are ", left_coef)
    # print("the right coeffiecient are: ", right_coef)
    print("the equation coefs are ", equ_coef)
    # print("the value of delata is ", delta)
    # print("the equation is ", equation)
    # print("the equation type is ", type(equation))