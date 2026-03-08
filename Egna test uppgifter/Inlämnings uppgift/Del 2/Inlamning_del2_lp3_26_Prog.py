# Skriv en inledande kommentar som talar om vad programmet gör. 
# Program for reading and analyzing csv files

# Placera dina modulimpoter här:
import csv
import matplotlib.pyplot as plt
from kamratgranskning_del1 import medelvarde_ekv, storsta_ekv, minsta_ekv # only importing what is actually used in the program

# Placera ev. nya funktioner som används i flera deluppgifter här:
# Skriv din ev. kod här:
# Declaring two lists in the begining of the program so that they will be stored globaly and not just in functions
lghData = []
villaData = []

def load_files(): # Loads predtermined CSV flie that will be used later
    global lghData, villaData
    try:
        lghData = file_to_list("lghpriser.csv")
        data["L"] = lghData
        print("\nSkriver ut lgh data:")
        for row in data["L"][:3]:
            print(row)
    except:
        print("Ladda ner Lghdata filen")
    
    try:
        villaData = file_to_list("villapriser.csv")
        data["V"] = villaData
        print("\nSkriver ut villa data:")
        for row in data["V"][:3]:
            print(row)
    except:
        print("Ladda ner Villadata filen")

# Only used to handle user inputs as well as some slight error handeling
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

# Ref line 29
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

# Ref line 29
def price_catagory():
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

def price_range():
    while True:
        try:
            price_input = (int(input("\nAnge ett prisområde, SE1 [1], SE2 [2], SE3 [3], SE4 [4]: ")))
            if price_input in range(1,5):
                return 1+((price_input-1)*4)
            else:
                print("\033[1;31;41m", end = "")
                print("Ogiltig input, välj en siffra, [1-4], SE1 [1], SE2 [2], SE3 [3], SE4 [4]: ")
                print("\033[0;37;40m")
        except:
            print("\033[1;31;41m", end = "")
            print("Ogiltig input, välj en siffra [1-4] Inte en bokstav din jävel!")
            print("\033[0;37;40m")


# Ref line 29
def list_input():
    while True:
        list_input = (input("\nVälj listan som du vill arbeta med, Lägenhets lista [L] eller Villa lista [V]: ")).upper()
        if list_input == "L" or list_input == "V":
            return list_input
        else:
            print("\033[1;31;41m", end = "")
            print("Ogiltig input, välj bokstav L eller V")
            print("\033[0;37;40m")

# Handles all the user choices and returnes them
def inputs(menu_option):
    if menu_option == 2:
        return year_input(), list_input()
    elif menu_option == 3:
        return year_input(), price_range()
    elif menu_option == 4:
        return year_input(), column_input(), list_input()
    elif menu_option == 5:
        return price_catagory()


# Deluppgift 1: Funktioner för deluppgift 1 i ordning.
# Skriv din kod här:
def file_to_list(file): # Opens a file for reading and converts it to a list, closes it and then returns the list
    csv_file = open(file, "r", encoding = "UTF-8", newline = "\n")
    csv_reader = csv.reader(csv_file, delimiter=";")
    work_list = []
    
    for row in csv_reader:
        for i in range(2, len(row)): # Converts all "float" strings into actual floats
            try:
                row[i] = float(row[i])
            except:
                pass
        work_list.append(row)
    csv_file.close()
    return work_list


# Deluppgift 2: Funktioner för deluppgift 2 i ordning. Ska använda funktioner från deluppgift VI på Del1 i modulen och ev. modifiera dem.
# Skriv din kod här:
def analys(year, price_list): # Prints an analisys of the given year an list
    if price_list is lghData: 
        customer = "lägenhetskund"
    elif price_list is villaData:
        customer = "villakund"
    titel = f"Analys av elpriserna för kategorin {customer} år {year}"

    print(f"\n{titel:^210}")
    print(f"{"="*len(titel):^210}")
    print(f"{"Fast pris 1 år (öre/Kwh)":^60}{"Fast pris 3 år (öre/Kwh)":^50}{"Rörligt pris (öre/Kwh)":^50}{"Anvisat pris (öre/Kwh)":^50}")
    print(f"{"Prisomr.":<10}{"Max - ":>10}{"(Mån)":<10}{"Min - ":>10}{"(mån)":<10}{"Medel |":^10}", end = "")
    print(f"{"Max - ":>10}{"(Mån)":<10}{"Min - ":>10}{"(mån)":<10}{"Medel |":^10}", end = "")
    print(f"{"Max - ":>10}{"(Mån)":<10}{"Min - ":>10}{"(mån)":<10}{"Medel |":^10}", end = "")
    print(f"{"Max - ":>10}{"(Mån)":<10}{"Min - ":>10}{"(mån)":<10}{"Medel |":^10}")
    print(f"-"*208)
    for SE in range(0, (len(price_list[0])-2), 4): # Makes SE be 0, 4, 8, 12,... and forever on depending on how long the list that is inputed is
        print(f"{price_list[0][SE+2]:<10.3s}", end="")
        #*_f_1 = fast pris 1 år , *_f_3 = fast pris 3 år , *_r = rörligt pris, *_a = anvisat pris
        
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


# Deluppgift 3: Funktioner för deluppgift 3 i ordning.
# Skriv din kod här:
def plot_rorlig_fast_1(year, price_cat): # Creates a visual graph of "Fast 1 år" and "Rörlig" for both lgh and villa
    x = []

    y_fast_1_lgh = []
    y_rorlig_lgh = []

    y_fast_1_villa = []
    y_rorlig_villa = []

    for row in lghData:
        if row[0] == str(year):
            x.append(row[1][:3])
            y_fast_1_lgh.append(row[price_cat+1])
            y_rorlig_lgh.append(row[price_cat+3])
    for row in villaData:
        if row[0] == str(year):
            y_fast_1_villa.append(row[price_cat+1])
            y_rorlig_villa.append(row[price_cat+3])

    plt.figure(figsize=(10,10))

    plt.plot(x, y_fast_1_lgh, color = "green", label = "Fast 1 år - Lgh")
    plt.plot(x, y_fast_1_villa, color = "red", label = "Fast 1 år - Villa")
    plt.plot(x, y_rorlig_lgh, color = "blue", label = "Rörlig - Lgh")
    plt.plot(x, y_rorlig_villa, color = "purple", label = "Rörlig - Villa")
    
    plt.legend(loc = 2)
    plt.grid()
    plt.title(f"Elpriser frisområde {lghData[0][price_cat+1][0:3]} år {year}")

    plt.xlabel("Månad")
    plt.ylabel("Pris [öre/kWh]")
    plt.xticks(rotation = 90)

    plt.show()


# Deluppgift 4: Funktioner för deluppgift 4 i ordning.
# Skriv din kod här:
def change_factor_ekv(price, price_prev): # Just the ekvation for the change factor that was provided
    change = ((price - price_prev)/price_prev)*100
    return change

def change_faktor(year, column, price_list): # Creates a visual bar graph of the change factor for a given year, SE*-* and list
    x_month = []
    y_change = []
# Cheacks if the year is equal to 2018 or not, if it is it will skip the first months change factor seeing as we can't pull info from dec 2017
    if year == 2018: 
        last_month = None
        year_row = 1
    else:
        for i in range(len(price_list)):
            try:
                if price_list[i].index(str(year)) == 0:
                    year_row = i
                    last_month = price_list[i-1][column]
                    break
            except:
                pass

    for row in price_list[year_row:]:
        if last_month == None:
            for index in price_list:
                if index[0] == str(year):
                    last_month = index[column]
                    break
            continue

        if row[0] == str(year):
            x_month.append(row[1][:3])
            y_change.append(change_factor_ekv(row[column], last_month))
            last_month = row[column]
        elif row[0] == str(year+1): # Stops the scan if we are one year ahead of the input year
            break
    
    plt.figure(figsize=(10,10))

    plt.grid()
    plt.title(f"Månatlig föränding av elpriset för {lghData[0][column]}")

    plt.bar(x_month, y_change, color = "red", width = 0.4)
    plt.xlabel("Månad")
    plt.ylabel("Föränding [%]")

    plt.show()


# Deluppgift 5: Funktioner för deluppgift 5 i ordning.
# Skriv din kod här:
def point_diagram(price_catagory): # Creates a scatter graph of all the years in each list and each price range, to find the max, min and average prices
    years_in_lists = []
    for row in lghData[1::12]:
        for year in row:
            if int(year) not in years_in_lists:
                years_in_lists.append(int(year))
                break
    years = f"{years_in_lists[0]}-{years_in_lists[len(years_in_lists)-1]}"
    catagory = lghData[0][price_catagory+1][4:]

    print("="*80)
    print(f"{f"Lägsta-, högsta- och medelvärden av elpricerna under":^80}")
    print(f"{f"tidsperioden {years} för {catagory}":^80}\n")
    print(f"{"Prisomr.":^10}{"lägsta":^10}{"år":^10}{"mån":^10}", end = "")
    print(f"{"högsta":^10}{"år":^10}{"mån":^10}{"medel":^10}")
    print(f"-"*80)
    min_list_lgh = []
    max_list_lgh = []
    avg_list_lgh = []

    min_list_villa = []
    max_list_villa = []
    avg_list_villa = []

    x_SE = []
    for price_list in data:
        if price_list == "L":
            print("Kategori Lägenhetskund:")
        else:
            print("Kategori villakund:")
        
        for SE in range(0, (len(data[price_list][0])-2), 4):
            print(f"{data[price_list][0][SE+5]:^10.3s}", end="")
            if data[price_list][0][SE+5][0:3] not in x_SE:
                x_SE.append(data[price_list][0][SE+5][0:3])
            current_min = float("inf")
            current_max = float("-inf")
            avg = 0

            for year in years_in_lists:
                temp = minsta_ekv(data[price_list], year, SE+price_catagory+1)[0]
                if temp <= current_min:
                    current_min, min_month = minsta_ekv(data[price_list], year, SE+price_catagory+1)
                    min_year = year

                temp = storsta_ekv(data[price_list], year, SE+price_catagory+1)[0]
                if temp >= current_max:
                    current_max, max_month = storsta_ekv(data[price_list], year, SE+price_catagory+1)
                    max_year = year
                avg = avg + medelvarde_ekv(data[price_list], year, SE+price_catagory+1)

            avg = avg/len(years_in_lists)

            if price_list == "L":
                min_list_lgh.append(current_min)
                max_list_lgh.append(current_max)
                avg_list_lgh.append(avg)
            else:
                min_list_villa.append(current_min)
                max_list_villa.append(current_max)
                avg_list_villa.append(avg)
            
            print(f"{current_min:^10.2f}{min_year:^10}{min_month:^10.3s}", end = "")
            print(f"{current_max:^10.2f}{max_year:^10}{max_month:^10.3s}{avg:^10.2f}")

    plt.figure(figsize=(20,10))
    #subplot 1
    plt.subplot(1,2,1)
    plt.scatter(x_SE, min_list_lgh, color = "Blue", label = "Lägsta elpris.")
    plt.scatter(x_SE, max_list_lgh, color = "Goldenrod", label = "Högsta elpris.")
    plt.scatter(x_SE, avg_list_lgh, color = "Green", label = "Medelvärde.")
    plt.legend()
    plt.title(f"Elpriser \nLägsta-, högsta- och medelvärden av elpricerna under tidsperioden {years}. \n Kategori lägenhetskund: {catagory}")
    plt.xlabel("Prisområden")
    plt.ylabel("Pris [öre/kWh]")
    plt.grid()

    #subplot 2
    plt.subplot(1,2,2)
    plt.scatter(x_SE, min_list_villa, color = "Blue", label = "Lägsta elpris.")
    plt.scatter(x_SE, max_list_villa, color = "Goldenrod", label = "Högsta elpris.")
    plt.scatter(x_SE, avg_list_villa, color = "Green", label = "Medelvärde.")
    plt.legend()
    plt.title(f"Elpriser \nLägsta-, högsta- och medelvärden av elpricerna under tidsperioden {years}. \n Kategori villakun: {catagory}")
    plt.xlabel("Prisområden")
    plt.ylabel("Pris [öre/kWh]")
    plt.grid()

    plt.show()
    

# Huvudprogram med Meny för deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:
def menu(): # Just the menu for the entire programe, its called at the end of everything as the initiation point sort of like a main function in other programs
    global data
    data = {"L" : lghData, "V" : villaData}
    work_list = None
    
    print("="*210)
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
            continue

        if base_input == 1:
            load_files()
            base_input = None

        elif (base_input == 2) and (len(data["L"]) != 0) and (len(data["V"]) != 0):
            year, work_list = inputs(base_input)
            analys(year, data[work_list])

            base_input = None

        elif (base_input == 3) and (len(data["L"]) != 0) and (len(data["V"]) != 0):
            year, price_catagory = inputs(base_input)
            plot_rorlig_fast_1(year, price_catagory)

            base_input = None

        elif (base_input == 4) and (len(data["L"]) != 0) and (len(data["V"]) != 0):
            year, column, price_list = inputs(base_input)
            change_faktor(year, column, data[price_list])

            base_input = None

        elif (base_input == 5) and (len(data["L"]) != 0) and (len(data["V"]) != 0):
            point_diagram(inputs(base_input))

            base_input = None

        elif (base_input == 6):
            break

        elif (len(data["L"]) == 0) and (len(data["V"]) == 0):
            print("\n\033[1;31;41m", end = "")
            print("Måste köra meny alternativ 1 för att få köra någon av meny alternativ [2-5]")
            print("\033[0;37;40m")

menu()