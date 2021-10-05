def is_palindrome(n):
    """
    :param n: numar intreg
    :return: True daca numarul este palindrom sau False daca numarul nu este palindrom
    """
    copie = n
    """"
    calculam inversul numarului
    """
    nou = 0
    while (copie > 0):
        """
        extragem ultima cifra
        """
        digit = copie % 10
        nou = nou * 10 + digit
        copie = copie // 10

    print("Numarul invers este " + str(nou))
    """
    comparam numarul nou cu cel original
    """
    if n==nou:
        return True
    return False
def test_is_palindrome():
    assert is_palindrome(121)==True
    assert is_palindrome(234)==False
    assert is_palindrome(565)==True
def get_cmmmc(list):
    lcm = list[0]
    for i in range(1, len(list)):
        """
        alegem numarul mai mare
        """
        if lcm > list[i]:
            max = lcm
        else:
            max= list[i]

        while (True):
            if ((max % lcm == 0) and (max % list[i] == 0)):
                lcm = max
                break
            max += 1

    return lcm


def main():

    while True:
        print('1.Verificam daca numarul este palindrom')
        print('2.Calculam cmmmc')
        print('3.Iesire')
        optiune=input('Alegeti o optiune')
        if optiune=='1':
            """
               citim un numar de la tastatura
               """
            n = int(input("Enter any number : "))
            if (is_palindrome(n)):
                print("True " + str(n)
                      )
            else:
                print("False")
        elif optiune=='2':
            """
                introducem numarul de numere
                """
            nr = int(input("Enter number of elements : "))

            """
            am creat o lista
            """
            lst = []

            for i in range(0, nr):
                element = int(input())
                """
                adaugam elementul
                """
                lst.append(element)

            # print the list
            print(lst)

            cmmmc = get_cmmmc(lst)
            print("Cel mai mic multiplu comun este: " + str(cmmmc))

test_is_palindrome()

main()