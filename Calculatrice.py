import os

divEucl = False
quit = False

while quit == False:
    choix = input("Your choice : (\'+\' = addition, \'-\' = subtraction, \'*\' = multiplication, \'/\' = division, \'//\' = euclidean divisition , \'Quit\' = Quit)\n")

    while choix != "+" and choix != "-" and choix != "*" and choix != "/" and choix != "//" and choix != "Quit":
        choix = input("Your choice : (\'+\' = addition, \'-\' = subtraction, \'*\' = multiplication, \'/\' = division, \'//\' = euclidean divisition , \'Quit\' = Quit)\n")

        
    numb1 = input("first number : ")
    while not numb1.isnumeric():
        numb1 = input("first number : ")
    numb2 = input("second number : ")
    while not numb2.isnumeric():
        numb2 = input("second number : ")

    if choix == "+": # Addition
        resultat = float(numb1) + float(numb2)
    elif choix == "-": # Soustraction
        resultat = float(numb1) - float(numb2)
    elif choix == "*": # Multiplication
        resultat = float(numb1) * float(numb2)
    elif choix == "/": # Division
        resultat = float(numb1) / float(numb2)
    elif choix == "//": # DIvision Euclidienne
        resultat = float(numb1) // float(numb2)
        reste = float(numb1) % float(numb2)
        divEucl = True
    elif choix == "Quit": # Quitter
        quit = True
    if quit == False:
        if divEucl == False:
            print(resultat)
        else:
            print(str(resultat) + ' remainder : ' + str(reste))

    input("Enter to continue ...")
    os.system("cls")
