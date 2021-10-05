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
    """
    citim un numar de la tastatura
    """
    n = int(input("Enter any number : "))
    if (is_palindrome(n)):
        print("True " + str(n)
 )
    else:
        print("False")

#run the test function
test_is_palindrome()
