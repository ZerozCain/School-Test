# Skriv en inledande kommentar som talar om vad programmet gör. 


# Placera dina modulimpoter här:
import csv
from tkinter.filedialog import askopenfilename

# Placera ev. nya funktioner som används i flera deluppgifter här:
# Skriv din ev. kod här:
def file_select():
    print("\033[1;31;41m", end = "")
    print("OBS: Kan behöva (alt+tab) eller (windows+tab) för att se ruta")
    print("\033[0;37;40m")

    csv_file = open(askopenfilename(), "r", encoding = "UTF-8", newline = "\n")
    csv_reader = csv.reader(csv_file, delimiter=";")
    return csv_reader

# Deluppgift 1: Funktioner för deluppgift 1 i ordning.
# Skriv din kod här:
def file_to_list(file):
    work_list = []
    
    for row in file:
        index = 2
        for i in row[2:]:
            try:
                row[index] = float(row[index])
            except:
                pass
            index += 1
        work_list.append(row)
    
    return work_list


# Deluppgift 2: Funktioner för deluppgift 2 i ordning. Ska använda funktioner från deluppgift V på Del1 i modulen och ev. modifiera dem.
# Skriv din kod här:


# Deluppgift 3: Funktioner för deluppgift 3 i ordning.
# Skriv din kod här:


# Deluppgift 4: Funktioner för deluppgift 4 i ordning.
# Skriv din kod här:


# Deluppgift 5: Funktioner för deluppgift 5 i ordning.
# Skriv din kod här:


# Huvudprogram med Meny för deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:

def menu():
    work_list = None

    print("="*150)
    print("\nProgram för att läsa in och analysera resultatet i uppgift 1 - 5\n")

    print("\n1. Läs in CSV-filer. (Måste köras innan övriga alternativ)")
    print("2. Analysera elpris valt år.")
    print("3. Årsvariation hos elpriset.")
    print("4. Beräknar förändringsfaktorerna per månad.")
    print("5. Lägsta, högsta och medelvärde.")
    print("6. Analysera rörligt elpris valt år")
    print("6. Avsluta programmet.\n")


    while True:
        try:
            base_input = int(input("Välj ett menyalternativ [1-6]: "))
                
        except Exception:
            print("\033[1;31;41m", end = "")
            print("Mata in ett nummer mellan [1-6] och inte en bokstav din jävel!")
            print("\033[0;37;40m")

        if base_input == 1:
            print("\nLeta upp (lghpriser.csv) i dina filler")
            lgh_data = file_to_list(file_select())
            print(lgh_data[0:3], "\n")

            print("Leta upp (villapriser.csv) i dina filler")
            villa_data = file_to_list(file_select())
            print(villa_data[0:3], "\n")
            
            base_input = None

        elif (base_input == 2) and (work_list is not type(None)):
            pass

        elif (base_input == 3) and (work_list is not type(None)):
            pass

        elif (base_input == 4) and (work_list is not type(None)):
            pass

        elif (base_input == 5) and (work_list is not type(None)):
            pass

        elif (base_input == 6) and (work_list is not type(None)):
            break

menu()