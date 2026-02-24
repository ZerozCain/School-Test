# Skriv en inledande kommentar som talar om vad programmet gör. 


# Placera dina modulimpoter här:
import csv
import matplotlib.pyplot as plt

# Placera ev. nya funktioner som används i flera deluppgifter här:
# Skriv din ev. kod här:

lgh_data = []
villa_data = []

def year_input():
    while True:
        try:
            year_input = int(input("\nVälj året som du vill arbeta med, [2018-2025]: "))
            if year_input in range(2018,2026) or year_input in range(18,26):
                if year_input in range(18,26):
                    return (year_input+2000)
                return year_input
            else:
                print("\033[1;31;41m", end = "")
                print("Ogiltig input välj ett år, [2018-2025]")
                print("\033[0;37;40m")
        except:
            print("\033[1;31;41m", end = "")
            print("Ogiltig input, välj ett år [2018-2025] och inte en bokstav din jävel!")
            print("\033[0;37;40m")
        
def column_input():
    while True:
        print("\nSE1-Fast-1 [1]  | SE1-Fast-3 [2]  | SE1-Rörligt [3]  | SE1-Anvisat [4]")
        print("SE2-Fast-1 [5]  | SE2-Fast-3 [6]  | SE2-Rörligt [7]  | SE2-Anvisat [8]")
        print("SE3-Fast-1 [9]  | SE3 Fast-3 [10] | SE3-Rörligt [11] | SE3-Anvisat [12]")
        print("SE4-Fast-1 [13] | SE4-Fast-3 [14] | SE4-Rörligt [15] | SE4-Anvisat [16]")
        try:
            column_input = (int(input("Välj en kolumn att arbeta med, [1-16]: ")))
            if column_input in range(1,17):
                column_input += 1
                return column_input
            else:
                print("\033[1;31;41m", end = "")
                print("Ogiltig input, välj en siffra, [1-16]")
                print("\033[0;37;40m")
        except:
            print("\033[1;31;41m", end = "")
            print("Ogiltig input, välj en siffra [1-16] och inte en bokstav din jävel!")
            print("\033[0;37;40m")

def price_range():
    while True:
        try:
            price_input = (int(input("\nAnge ett prisområde, Fast-1 [1], Fast-3 [2], Rörligt [3], Anvisat [4]: ")))
            if price_input in range(1,5):
                return price_input
            else:
                print("\033[1;31;41m", end = "")
                print("Ogiltig input, välj en siffra, [1-4], Fast-1 [1], Fast-3 [2], Rörligt [3], Anvisat [4]: ")
                print("\033[0;37;40m")
        except:
            print("\033[1;31;41m", end = "")
            print("Ogiltig input, välj en siffra [1-4] Inte en bokstav din jävel!")
            print("\033[0;37;40m")

def list_input():
    while True:
        list_input = (input("\nVälj listan som du vill arbeta med, Lägenhets lista [L] eller Villa lista [V]: ")).upper()
        if list_input == "L" or list_input == "V":
            return list_input
        else:
            print("\033[1;31;41m", end = "")
            print("Ogiltig input, välj bokstav L eller V")
            print("\033[0;37;40m")

def inputs(menu_option):
    if menu_option == 1:
        pass
    elif menu_option == 2:
        return year_input(), list_input()
    elif menu_option == 3:
        return year_input(), price_range()
    elif menu_option == 4:
        return year_input(), column_input(), list_input()
    elif menu_option == 6:
        pass

#=====================================================================================================================================================================================================================================================
######################################################
# Code from my partners file to get analys() to work #
######################################################
def summa_ekv(namn,year,kolumn):  #Funktion som sumerar en hel kolumn 
    sum = 0 # Declaring the variable sum and making it equal to 0

    for row in namn:

        if row[0] == str(year): # Cheacks that the year on row[0] is the same as the input year

            if (type(row[kolumn]) is float) or (type(row[kolumn]) is int): # Makes sure that alla the values in row[column] can be summed this check comes up in almost all my functions
                sum += row[kolumn]

    return sum

def medelvarde_ekv(namn,year,kolumn): #Tar summan från tidigare funktion och delar den på antalet månader som ett år har 
    summa = summa_ekv(namn,year,kolumn)
    medel = summa/12
    return(round(medel,2)) #Runda av medelvärdet till två desimaler 
     
def storsta_ekv(namn,year,kolumn): # Modifierad så att fungerar med nya störe listorna
    max = float("-inf")
    month = ""

    for row in namn:
        if row[0] == str(year):
            if (type(row[kolumn]) is float) or (type(row[kolumn]) is int):

                if row[kolumn] >= max:
                    max = row[kolumn]
                    month = row[1]
    return max, month

def minsta_ekv(namn,year,kolumn): # Modifierad så att fungerar med nya störe listorna
    min = float("inf")
    month = ""

    for row in namn:
        if row[0] == str(year):
            if (type(row[kolumn]) is float) or (type(row[kolumn]) is int):

                if row[kolumn] <= min:
                    min = row[kolumn]
                    month = row[1]
    return min, month
#=====================================================================================================================================================================================================================================================

# Deluppgift 1: Funktioner för deluppgift 1 i ordning.
# Skriv din kod här:
def file_to_list(file):
    csv_file = open(file, "r", encoding = "UTF-8", newline = "\n")
    csv_reader = csv.reader(csv_file, delimiter=";")
    work_list = []
    
    for row in csv_reader:
        index = 2
        for i in row[2:]:
            try:
                row[index] = float(row[index])
            except:
                pass
            index += 1
        work_list.append(row)
    csv_file.close()
    return work_list


# Deluppgift 2: Funktioner för deluppgift 2 i ordning. Ska använda funktioner från deluppgift VI på Del1 i modulen och ev. modifiera dem.
# Skriv din kod här:

#=====================================================================================================================================================================================================================================================
###########################################
# Min partners orginal code for reference #
###########################################

#def analys(namn,year,levnad):
#    kolumn = 2
#    while kolumn <= 9:
#        storsta , manad = (storsta_ekv(namn,year,kolumn))
#        analys_lista.append(storsta)
#        analys_lista.append(manad)
#        minsta , manad = (minsta_ekv(namn,year,kolumn))
#        analys_lista.append(minsta)
#        analys_lista.append(manad)
#        Medel = (medelvarde_ekv(namn,year,kolumn))
#        analys_lista.append(Medel)
#        kolumn+=1
#    os.system("cls")                                            #Tar bort alltig som tidigare printades i terminalen
#    titel = f"Analys av elpriserna för kategorin {levnad} år {year}" 
#    print(f"{titel:^110}")
#    print(f"{"="*len(titel):^110}")                             #Linjen under titlen anpasar längden av titel beroende på vad som jämförs 
#    print(f"{"Fast pris 3 år (öre/Kwh)":^55}{"Rörligt pris (öre/Kwh)":^55}")
#    print(f"{"Prisomr.":<10}{"Max  -":>10}{"(Mån)":>10}{"Min  -":>10}{"(mån)":>10}{"Medel":>10}{"Max  -":>10}{"(Mån)":>10}{"Min  -":>10}{"(mån)":>10}{"Medel":>10}")
#    print(f"-"*110)
#    print(f"{"SE1":<10}{analys_lista[0]:>10}{analys_lista[1]:>10}{analys_lista[2]:>10}{analys_lista[3]:>10}{analys_lista[4]:>10}{analys_lista[5]:>10}{analys_lista[6]:>10}{analys_lista[7]:>10}{analys_lista[8]:>10}{analys_lista[9]:>10}")
#    print(f"{"SE2":<10}{analys_lista[10]:>10}{analys_lista[11]:>10}{analys_lista[12]:>10}{analys_lista[13]:>10}{analys_lista[14]:>10}{analys_lista[15]:>10}{analys_lista[16]:>10}{analys_lista[17]:>10}{analys_lista[18]:>10}{analys_lista[19]:>10}")
#    print(f"{"SE3":<10}{analys_lista[20]:>10}{analys_lista[21]:>10}{analys_lista[22]:>10}{analys_lista[23]:>10}{analys_lista[24]:>10}{analys_lista[25]:>10}{analys_lista[26]:>10}{analys_lista[27]:>10}{analys_lista[28]:>10}{analys_lista[29]:>10}")
#    print(f"{"SE4":<10}{analys_lista[30]:>10}{analys_lista[31]:>10}{analys_lista[32]:>10}{analys_lista[33]:>10}{analys_lista[34]:>10}{analys_lista[35]:>10}{analys_lista[36]:>10}{analys_lista[37]:>10}{analys_lista[38]:>10}{analys_lista[39]:>10}")
#    print(f"="*110)
#=====================================================================================================================================================================================================================================================
#=====================================================================================================================================================================================================================================================
##########################################################
# Modification of my partners code to solve deluppgift 2 #
##########################################################

def analys(year, price_list):
    if price_list == lgh_data: 
        customer = "lägenhetskund"
    elif price_list == villa_data:
        customer = "villakund"

    titel = f"Analys av elpriserna för kategorin {customer} år {year}"

    print(f"{titel:^210}")
    print(f"{"="*len(titel):^210}")
    print(f"{"Fast pris 1 år (öre/Kwh)":^60}{"Fast pris 3 år (öre/Kwh)":^50}{"Rörligt pris (öre/Kwh)":^50}{"Anvisat pris (öre/Kwh)":^50}")
    print(f"{"Prisomr.":<10}{"Max - ":>10}{"(Mån)":<10}{"Min - ":>10}{"(mån)":<10}{"Medel |":^10}", end = "")
    print(f"{"Max - ":>10}{"(Mån)":<10}{"Min - ":>10}{"(mån)":<10}{"Medel |":^10}", end = "")
    print(f"{"Max - ":>10}{"(Mån)":<10}{"Min - ":>10}{"(mån)":<10}{"Medel |":^10}", end = "")
    print(f"{"Max - ":>10}{"(Mån)":<10}{"Min - ":>10}{"(mån)":<10}{"Medel |":^10}")
    print(f"-"*208)
    for SE in range(0, (len(price_list[0])-2), 4): # Makes SE be 0, 4, 8, 12,... and forever on dependiing on how long the list that is inputed is
        print(f"{price_list[0][SE+2]:<10.3s}", end="")
        
        
        min_f_1, min_month_f_1 = minsta_ekv(price_list, year, SE+2)
        max_f_1, max_month_f_1 = storsta_ekv(price_list, year, SE+2)
        avg_f_1 = medelvarde_ekv(price_list, year, SE+2)
        print(f"{min_f_1:>7.2f}{min_month_f_1:>7.3s}{max_f_1:>13.2f}{max_month_f_1:>7.3s}{avg_f_1:>12.2f} |", end="")

        min_f_3, min_month_f_3 = minsta_ekv(price_list, year, SE+3)
        max_f_3, max_month_f_3 = storsta_ekv(price_list, year, SE+3)
        avg_f_3 = medelvarde_ekv(price_list, year, SE+3)
        print(f"{min_f_3:>9.2f}{min_month_f_3:>7.3s}{max_f_3:>13.2f}{max_month_f_3:>7.3s}{avg_f_3:>12.2f} |", end="")
        
        min_r, min_month_r = minsta_ekv(price_list, year, SE+4)
        max_r, max_month_r = storsta_ekv(price_list, year, SE+4)
        avg_r = medelvarde_ekv(price_list, year, SE+4)
        print(f"{min_r:>9.2f}{min_month_r:>7.3s}{max_r:>13.2f}{max_month_r:>7.3s}{avg_r:>12.2f} |", end="")

        min_a, min_month_a = minsta_ekv(price_list, year, SE+5)
        max_a, max_month_a = storsta_ekv(price_list, year, SE+5)
        avg_a = medelvarde_ekv(price_list, year, SE+5)
        print(f"{min_a:>9.2f}{min_month_a:>7.3s}{max_a:>13.2f}{max_month_a:>7.3s}{avg_a:>12.2f} |", end="")
        
        print()
#=====================================================================================================================================================================================================================================================

# Deluppgift 3: Funktioner för deluppgift 3 i ordning.
# Skriv din kod här:
def plot_rorlig_fast_1(year, price_r):
    x = []

    y_fast_1_lgh = []
    y_rorlig_lgh = []

    y_fast_1_villa = []
    y_rorlig_villa = []

    for row in lgh_data:
        if row[0] == str(year):
            x.append(row[1][0:3])
            y_fast_1_lgh.append(row[price_r+1])
            y_rorlig_lgh.append(row[price_r+3])
    for row in villa_data:
        if row[0] == str(year):
            y_fast_1_villa.append(row[price_r+1])
            y_rorlig_villa.append(row[price_r+3])

    plt.plot(x, y_fast_1_lgh, color = "green", label = "Fast 1 år - Lgh")
    plt.plot(x, y_fast_1_villa, color = "red", label = "Fast 1 år - Villa")
    plt.plot(x, y_rorlig_lgh, color = "blue", label = "Rörlig - Lgh")
    plt.plot(x, y_rorlig_villa, color = "purple", label = "Rörlig - Villa")
    
    plt.legend()
    plt.grid()
    plt.title(f"Elpriser frisområde {lgh_data[0][price_r+1][0:3]} år {year}")

    plt.xlabel("Månad")
    plt.ylabel("Pris [öre/kWh]")
    plt.xticks(rotation = 90)

    plt.show()


# Deluppgift 4: Funktioner för deluppgift 4 i ordning.
# Skriv din kod här:
def change_faktor(year, column, price_list):
    pass

# Deluppgift 5: Funktioner för deluppgift 5 i ordning.
# Skriv din kod här:


# Huvudprogram med Meny för deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:
def menu():
    global lgh_data, villa_data
    data = {"L" : None, "V" : None}
    work_list = None

    print("="*208)
    print("\nProgram för att läsa in och analysera resultatet i uppgift 1 - 5\n")

    while True:
        print("="*208)
        print("\n1. Läs in CSV-filer. (Måste köras innan övriga alternativ)")
        print("2. Analysera elpris valt år.")
        print("3. Årsvariation hos elpriset.")
        print("4. Beräknar förändringsfaktorerna per månad.")
        print("5. Lägsta, högsta och medelvärde.")
        print("6. Avsluta programmet.\n")

        try:
            base_input = int(input("Välj ett menyalternativ [1-6]: "))
                
        except Exception:
            print("\n\033[1;31;41m", end = "")
            print("Mata in ett nummer mellan [1-6] och inte en bokstav din jävel!")
            print("\033[0;37;40m")

        if base_input == 1:
            data["L"] = file_to_list("lghpriser.csv")
            lgh_data = file_to_list("lghpriser.csv")
            print("Skriver ut lgh data:\n")
            for row in data["L"][:3]:
                print(row)

            data["V"] = file_to_list("villapriser.csv")
            villa_data = file_to_list("villapriser.csv")
            print("Skriver ut lgh data:\n")
            for row in data["V"][:3]:
                print(row)
            
            base_input = None

        elif (base_input == 2) and (len(lgh_data) != 0) and (len(villa_data) != 0):
            year, work_list = inputs(base_input)
            analys(year, data[work_list])

            base_input = None

        elif (base_input == 3):
            year, p_r = inputs(base_input)
            plot_rorlig_fast_1(year, p_r)

            base_input = None

        elif (base_input == 4):
            year, column, price_list = inputs(base_input)
            change_faktor(year, column, price_list)

            base_input = None

        elif (base_input == 5):
            pass

        elif (base_input == 6):
            break


menu()