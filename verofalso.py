print("Nella cartella in cui esegui questo script deve essere presente il file verofalso.txt")


try:
    with open("verofalso.txt", 'r', encoding='utf-8') as file:
        filex = file.readlines()
        x = 1
        for line in filex:
            line = line.split(';')
            print(x, line[0] + "[vero] [falso]")
            x += 1

        x = 1
        print("Correttore")
        corr = ''
        for line in filex:
            line = line.split(';')
            corr += str(x) + line[1].strip() + " - "
            x += 1
        print(corr)
except:
    nomedelfile = input("Nome del file")
    with open(nomedelfile, 'r', encoding='utf-8') as file:
        filex = file.readlines()
        x = 1
        for line in filex:
            line = line.split(';')
            print(x, line[0] + "[vero] [falso]")
            x += 1

        x = 1
        print("Correttore")
        corr = ''
        for line in filex:
            line = line.split(';')
            corr += str(x) + line[1].strip() + " - "
            x += 1
        print(corr)
