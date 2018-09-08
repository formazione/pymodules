def istruzioni():
    print("\n")
    print("Se vuoi scrivere qualcos`altro, usa la funzione scrivi()")


def scrivi1():
    try:
        with open("memo.txt", 'a', encoding='utf-8') as file:
            for line in file:
                print(line)
            print("\n")
    except:
        file = open("memo.txt", 'a', encoding='utf-8')
        file.write("I miei appunti:")
        file.close


def scrivi():
    with open("memo.txt", 'a', encoding='utf-8') as file:
        for line in file:
            print(line)
            print("\n")
        m = input("Cosa vuoi ricordare?")
        file.write(m)


scrivi1()
istruzioni()
