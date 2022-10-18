#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number > 0:
        return number
    
    number = number - 2 * number
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    noms = []

    for i in prefixes:
        noms.append(i + suffixe)
    
    return noms


def prime_integer_summation() -> int:
    nombres_premiers = []
    currentNumber = 2
    sum = 0
    count = 0

    while count < 100:
        prime = True
        for i in range(2, currentNumber):
            if currentNumber % i == 0:
                prime = False
                break
        if prime:  
            sum += currentNumber
            count += 1
        currentNumber += 1

    return sum

def factorial(number: int) -> int:
    res = 1
    
    for i in range(1, number + 1):
        res *= i
    
    return res


def use_continue() -> None:
    for i in range(1, 10):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    ages_booleans = []

    for group in groups:
        if len(group) > 10 or len(group) <= 3:
            ages_booleans.append(False)
            continue
        elif 25 in group:
            ages_booleans.append(True)
            continue

        else:
            conditionMet = False
            for person in group:
                if person < 18:
                    ages_booleans.append(False)
                    conditionMet = True
                    break
                elif person > 70 and 50 in group:
                    ages_booleans.append(False)
                    conditionMet = True
                    break
            
            if conditionMet:
                continue

            ages_booleans.append(True)
            
    
    return ages_booleans

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
