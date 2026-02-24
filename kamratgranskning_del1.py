# Uppdaterad 2026-02-10
# Listor till del 1
import os #Importeras för att kunna använda clear screen
tom_lista = [] 
analys_lista = []  #Dessa variabler måste vara fördefingerade innan de senare används
kolumn = 0
levnad = ""
lgh = [['År','Månad','SE1-Fast pris 3 år','SE1-Rörligt pris','SE2-Fast pris 3 år','SE2-Rörligt pris','SE3-Fast pris 3 år','SE3-Rörligt pris','SE4-Fast pris 3 år','SE4-Rörligt pris'],
['2024','januari',127.19,121.29,126.66,121.64,143.51,144.71,171.92,150.62],
['2024','februari',117.75,97.07,117.06,96.70,132.46,102.05,150.66,108.56],
['2024','mars',116.44,107.50,115.88,107.71,131.09,111.62,149.04,117.29],
['2024','april',116.33,99.97,115.43,101.06,129.27,108.31,146.86,117.78],
['2024','maj',119.57,60.30,118.73,60.32,131.63,67.71,148.81,100.899],
['2024','juni',116.04,66.67,115.48,66.79,128.03,70.51,149.59,114.56],
['2024','juli',111.63,61.86,111.22,61.70,126.05,61.81,143.33,91.61],
['2024','augusti',112.83,45.47,112.32,45.22,127.58,45.33,145.97,93.91],
['2024','september',109.82,47.47,109.48,49.26,124.76,56.02,142.13,73.92],
['2024','oktober',107.98,50.03,107.73,51.18,122.62,64.03,140.88,74.26],
['2024','november',109.29,68.10,107.81,59.54,124.10,123.63,140.23,145.87],
['2024','december',105.70,53.35,103.55,51.27,121.35,116.01,137.43,131.13],
['2025','januari',103.12,66.79,100.45,66.62,121.33,118.02,139.62,133.49],
['2025','februari',104.19,53.03,101.23,55.48,121.30,136.92,143.51,172.84],
['2025','mars',101.66,56.90,99.86,50.80,120.41,103.07,141.47,114.42],
['2025','april',99.43,53.78,97.75,53.52,118.76,83.61,137.13,110.80],
['2025','maj',101.55,54.43,99.89,56.09,120.31,90.52,139.41,112.10],
['2025','juni',103.45,38.79,101.73,41.07,122.07,63.58,142.64,86.18],
['2025','juli',103.56,52.94,102.08,55.31,123.27,82.44,144.69,94.56],
['2025','augusti',104.51,61.21,103.21,59.78,123.70,85.67,146.23,112.96],
['2025','september',94.80,67.38,92.96,66.25,119.07,109.34,139.30,135.41],
['2025','oktober',104.86,54.73,103.55,53.75,125.03,118.62,146.99,127.77],
['2025','november',103.30,88.72,101.48,85.45,122.94,131.79,144.00,145.51],
['2025','december',100.94,76.59,98.85,77.22,118.90,101.52,139.64,119.00]]
villa = [['År','Månad','SE1-Fast pris 3 år','SE1-Rörligt pris','SE2-Fast pris 3 år','SE2-Rörligt pris','SE3-Fast pris 3 år','SE3-Rörligt pris','SE4-Fast pris 3 år','SE4-Rörligt pris'],
['2024','januari',110.06,100.48,109.58,100.93,124.09,124.70,153.33,130.32],
['2024','februari',100.03,76.48,99.43,76.25,112.48,82.29,130.53,88.48],
['2024','mars',98.28,82.14,97.77,90.35,110.96,100.89,127.95,128.22],
['2024','april',83.28,78.93,90.95,80.13,100.70,88.43,123.96,97.24],
['2024','maj',101.10,37.02,99.57,37.17,111.47,46.23,130.19,78.26],
['2024','juni',93.92,42.97,93.13,43.07,106.92,48.20,130.05,91.82],
['2024','juli',86.63,38.66,85.88,38.56,102.61,39.86,121.58,69.06],
['2024','augusti',88.40,23.75,87.67,23.49,104.19,24.43,125.06,72.56],
['2024','september',86.35,25.03,85.83,26.83,102.83,34.63,121.79,51.91],
['2024','oktober',82.91,27.83,81.86,28.98,100.04,43.00,119.93,52.59],
['2024','november',83.68,45.97,82.41,37.56,101.13,103.08,117.92,124.51],
['2024','december',83.16,30.18,81.42,28.22,99.38,94.98,118.52,108.84],
['2025','januari',81.21,45.03,79.14,44.82,98.98,97.21,118.87,112.40],
['2025','februari',86.81,33.50,83.22,36.02,101.07,117.36,125.19,153.16],
['2025','mars',82.87,35.91,81.12,29.88,99.59,82.70,122.68,93.57],
['2025','april',78.60,32.89,76.54,32.83,98.04,63.33,119.11,89.87],
['2025','maj',80.95,33.45,79.21,35.27,100.14,70.30,120.91,91.33],
['2025','juni',82.09,17.91,79.66,20.53,101.83,43.41,123.79,65.61],
['2025','juli',82.79,32.08,80.47,34.70,102.98,62.21,125.14,73.90],
['2025','augusti',84.03,46.17,82.20,44.91,103.93,76.85,127.96,106.87],
['2025','september',82.76,44.06,81.00,42.95,104.42,88.36,127.84,113.49],
['2025','oktober',84.01,35.15,82.41,34.37,103.99,97.54,126.84,108.33],
['2025','november',82.53,69.05,80.15,65.76,101.81,111.56,123.95,125.97],
['2025','december',80.35,56.24,77.59,57.01,97.61,80.98,119.78,98.75]]
# Programmets syfter är att undersöka elpriserna för lägenheter och hus månadsvis under spanet av 2 år.
def kolumn_logic(omrade,prisklass): #Denna funktion tar användarens val och ger ut siffran på kolumnen som motsvarar användares val
        if omrade == 1 and prisklass == 1:
            kolumn = 2
        elif omrade == 1 and prisklass == 2:
            kolumn = 3
        elif omrade == 2 and prisklass == 1:
            kolumn = 4
        elif omrade == 2 and prisklass == 2:
            kolumn = 5
        elif omrade == 3 and prisklass == 1:
            kolumn = 6
        elif omrade == 3 and prisklass == 2:
            kolumn = 7
        elif omrade == 4 and prisklass == 1:
            kolumn = 8
        elif omrade == 4 and prisklass == 2:
            kolumn = 9
        elif kolumn == 0:
            print("Ett oväntat fel uppstod")  #Extra säkerhet om något ända blivit fel
        return(kolumn)
def bostad_val(): #Låter användaren välja vilken bostadstyp att jämföra
    while True:
        print("Välj bostadstyp: ")
        print("1. Lägenheter")
        print("2. Villa")
        bostad = input("Välj (1-2): ") #Användaren får välja mellan att jämföra lägenheter eller villor
        if bostad == "1":   #Om användaren väljer "1" blir namn = lägenhet
            namn = lgh
            break 
        elif bostad == "2": #Om användaren väljer "2" blir namn = villa 
            namn = villa
            break
        else:
            print("\nOglitigt val, gör om och gör rätt\n") #Om användaren skriven in något annat så kommer de få börja om med detta valet.
            continue
    return(namn)
def year_choice(): #Låter användaren bestäma vilket år som ska jämföras 
    while True: 
        year = (input("\nSkriv 2024 eller 2025 att jämföra: "))
        if year != "2024" and year != "2025":
            print("Ogiltigt år, välj ett giltigt år") #Om variblen year inte har ett "rätt" värde får användaren försöka igen
            continue
        return(year)
   
def omrade_val(): #Låter användaren välja vilket pris område i Sverige att jämföra
    while True:
        print("\nOmråden att välja mellan\n")
        print("1. SE1")
        print("2. SE2")
        print("3. SE3")
        print("4. SE4")
        omrade = int(input("Välj område(1-4): "))
        if 1 <= omrade <= 4:
            break 
        else: #Kontrollerar så att variablen omrade är inom de defingerade parametrarna
            print("Ogiltigt område, välj ett giltigt område")
            continue
    return(omrade)
def prisklass_val(): #Låter användaren välja vilket avtalstyp att jämföra mellan
   while True:
        print("\nAvtals typ")
        print("1. Fast 3 år")
        print("2. Rörligt")
        prisklass = int(input("Välj en avtalstyp(1-2): "))
        if prisklass == 1 or prisklass == 2:
            return(prisklass)
        else:
            print("Ogiltigt avtalstyp försök igen")
            continue
        
    
# Deluppgift 1: Funktioner för deluppgift I i ordning.
# Funktion som skriver ut listan som skickas med in på olika sett utifrån ett menyval.
# Inparameter: Listan som skall skrivas ut.
# Returvärde: Funktionen har inget returvärde.
def print_lista(namn): #Låter användaren printa hela eller delar av den valda listan
    while True:
        print('\nSkriver ut en lista')
        print('1: Hela listan')
        print('2: Listan radvis')
        print('3: Listan elementvis som matris')
        val = input('Hur vill du skriva ut listan? ')
        os.system('cls') #Tar bort allt som tidigare skrivits i terminalen 
        if val == '1':
            print('\nHela listan\n') 
            print(namn) # Skriver ut hela listan i en utskrift utan radbrytning för  varje rad
            break
        elif val == '2':
            print('\nListan radvis\n')
            for row in namn: # Skriver ut hela listan radvis med radbrytning för varje rad
                print(row)
        elif val == '3':       
            print('\nListan som matris\n')
            for row in namn: # Skriver ut hela listan elementvis med radbrytning för varje rad
                for item in row:
                    print(f'{item:<20}', end=" ")
                print('')
            break 
        else:
            print('Ogiltigt val. Du kommer tillbaka till huvudmenyn.')
            break
# Deluppgift II: Funktioner för deluppgift II i ordning.
# Skriv din kod här:
def summa_ekv(namn,year,kolumn):  #Funktion som sumerar en hel kolumn 
    summa = 0         
    if year == "2024": #Om det är 2024 som jämförs så kommer summa formeln starta ifrån rad 
        i = 1 #I är lika med raden i listan som jämförs
        while i <= 12:
            summa = namn[i][kolumn] + summa
            i+=1
        
    if year == "2025": #Om det istället är 2025 som jämförs så kommer summa formlen  att starta ifrån rad 13
        i = 13 #I är raden i listan som jämförs 
        while i <= 24:
            summa = namn[i][kolumn] + summa
            i+=1     
    return(summa)
# Deluppgift III: Funktioner för deluppgift III i ordning.
# Skriv din kod här:
def medelvarde_ekv(namn,year,kolumn): #Tar summan från tidigare funktion och delar den på antalet månader som ett år har 
    summa = summa_ekv(namn,year,kolumn)
    medel = summa/12
    return(round(medel,2)) #Runda av medelvärdet till två desimaler 
     
# Deluppgift IV: Funktioner från deluppgift IV i ordning.
# Skriv din kod här:
def storsta_ekv(namn,year,kolumn): #Jämför alla talen i den angivan kolumen och hittar det största talet
    storsta = 0
    
    if year == "2024": #Om det är 2024 som jämförs så kommer summa formeln starta ifrån rad 
        i = 1 #i är lika med raden i listan som jämförs
        while i <= 12:
            if storsta < namn[i][kolumn]:
                storsta = namn[i][kolumn]
                manad = namn[i][1]
            i+=1
            
    if year == "2025": #Om det istället är 2025 som jämförs så kommer summa formlen  att starta ifrån rad 13
        i = 13 #i är lika med raden i listan som jämförs
        while i <= 24:
            if storsta < namn[i][kolumn]:
                storsta = namn[i][kolumn]
                manad = namn[i][1]
            i+=1
    return(round(storsta,2),manad) #Rundar av till två decimaler
# Deluppgift V: Funktioner från deluppgift V i ordning.
# Skriv din kod här:
def minsta_ekv(namn,year,kolumn): #Jämför alla talen i en angiven kolumn och hittar  det minsta talet
    if year == "2024": #Om det är 2024 som jämförs så kommer summa formeln starta ifrån rad 
        i = 1 #i är lika med raden i listan som jämförs
        minsta = namn[i][kolumn]
        while i <= 12:
            if minsta > namn[i][kolumn]:
                minsta = namn[i][kolumn]
                manad = namn[i][1]
            i+=1
            
    if year == "2025": #Om det istället är 2025 som jämförs så kommer summa formlen  att starta ifrån rad 13
        i = 13 #i är lika med raden i listan som jämförs
        minsta = namn[i][kolumn]
        while i <= 24:
            if minsta < namn[i][kolumn]:
                minsta = namn[i][kolumn]
                manad = namn[i][1]
            i+=1
    return(round(minsta,2),manad)
# Deluppgift VI: Funktioner från deluppgift IV i ordning.
# Skriv din kod här:
def analys(namn,year,levnad):
    kolumn = 2
    while kolumn <= 9:
        storsta , manad = (storsta_ekv(namn,year,kolumn))
        analys_lista.append(storsta)
        analys_lista.append(manad)
        minsta , manad = (minsta_ekv(namn,year,kolumn))
        analys_lista.append(minsta)
        analys_lista.append(manad)
        Medel = (medelvarde_ekv(namn,year,kolumn))
        analys_lista.append(Medel)
        kolumn+=1
    os.system('cls')                                            #Tar bort alltig som tidigare printades i terminalen
    titel = f"Analys av elpriserna för kategorin {levnad} år {year}" 
    print(f"{titel:^110}")
    print(f'{"="*len(titel):^110}')                             #Linjen under titlen anpasar längden av titel beroende på vad som jämförs 
    print(f'{"Fast pris 3 år (öre/Kwh)":^55}{"Rörligt pris (öre/Kwh)":^55}')
    print(f'{"Prisomr.":<10}{"Max  -":>10}{"(Mån)":>10}{"Min  -":>10}{"(mån)":>10}{"Medel":>10}{"Max  -":>10}{"(Mån)":>10}{"Min  -":>10}{"(mån)":>10}{"Medel":>10}')
    print(f"-"*110)
    print(f'{"SE1":<10}{analys_lista[0]:>10}{analys_lista[1]:>10}{analys_lista[2]:>10}{analys_lista[3]:>10}{analys_lista[4]:>10}{analys_lista[5]:>10}{analys_lista[6]:>10}{analys_lista[7]:>10}{analys_lista[8]:>10}{analys_lista[9]:>10}')
    print(f'{"SE2":<10}{analys_lista[10]:>10}{analys_lista[11]:>10}{analys_lista[12]:>10}{analys_lista[13]:>10}{analys_lista[14]:>10}{analys_lista[15]:>10}{analys_lista[16]:>10}{analys_lista[17]:>10}{analys_lista[18]:>10}{analys_lista[19]:>10}')
    print(f'{"SE3":<10}{analys_lista[20]:>10}{analys_lista[21]:>10}{analys_lista[22]:>10}{analys_lista[23]:>10}{analys_lista[24]:>10}{analys_lista[25]:>10}{analys_lista[26]:>10}{analys_lista[27]:>10}{analys_lista[28]:>10}{analys_lista[29]:>10}')
    print(f'{"SE4":<10}{analys_lista[30]:>10}{analys_lista[31]:>10}{analys_lista[32]:>10}{analys_lista[33]:>10}{analys_lista[34]:>10}{analys_lista[35]:>10}{analys_lista[36]:>10}{analys_lista[37]:>10}{analys_lista[38]:>10}{analys_lista[39]:>10}')
    print(f'='*110)
# Huvudprogram med Meny. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:
#Loop för menyn
while True: 
    print(f"-"*(64))
    print(f"Program för att läsa in och analysera resultatet i uppgift 1 - 6")
    print(f"="*(64))
    print(f"1. Skriv ut listan.")
    print(f"2. Beräkna summa.")
    print(f"3. Beräkna medelvärde.")
    print(f"4. Hitta största värdet.")
    print(f"5. Hitta minsta värdet.")
    print(f"6. Analysera rörligt elpris valt år.")
    print(f"7. Avsluta program.")
    print(f"-"*(64))
    user_choice_menu = input(f"\nVälj ett menyalternativ (1-7): ") #Användaren får välja mellan 
    if user_choice_menu == "1": #Om användaren skriver "1" så kommer de att påkalla  print_lista funktionen
        namn = bostad_val()
        print_lista(namn)
        break 
    elif user_choice_menu == "2": #Om användaren skriver "2" så kommer de att påkalla summa funktionen
        omrade = omrade_val() 
        prisklass = prisklass_val() #Dessa funktioner är det som gör att användaren  få möjligheten till att välja 
        year = year_choice()
        namn = bostad_val()
        kolumn = kolumn_logic(omrade,prisklass)
        summa = summa_ekv(namn,year,kolumn)
        if namn == lgh:           #denna del gör att användare få se vilket bostadstyp de valde tidigare
            levnad = "lägenheter"       
        elif namn  == villa:
            levnad == "Villor" 
        print(f"\nSumman av elpriserna i {levnad} under året {year} i {namn[0][kolumn]} var {summa}")    
        break  
                                
    elif user_choice_menu == "3": #Om användaren skriver "3" så kommer de att påkalla medelvärde funktionen
        omrade = omrade_val()
        prisklass = prisklass_val() #Dessa funktioner är det som gör att användaren få möjligheten till att välja 
        namn = bostad_val()
        year = year_choice()
        kolumn = kolumn_logic(omrade,prisklass)
        medel = medelvarde_ekv(namn,year,kolumn)
        if namn == lgh:           #denna del gör att användare få se vilket bostadstyp de valde tidigare
            levnad = "lägenheter"
        elif namn == villa:
            levnad == "Villor"
        print(f"\nMedelvärdet av elpriserna i {levnad} under året {year} i {namn[0][kolumn]} var {medel}")
        break
    elif user_choice_menu == "4": #Om användaren skriver "4" så kommer de att påkalla hitta största värdet funktionen
        omrade = omrade_val()
        prisklass = prisklass_val()
        namn = bostad_val()
        year = year_choice()
        kolumn = kolumn_logic(omrade,prisklass)
        storsta , manad = storsta_ekv(namn,year,kolumn)
        print(f"\nEl priset var som högst under {year} i {manad} på {storsta} öre / Kwh ")
        break
    elif user_choice_menu == "5": #Om användaren skriver "5" så kommer de att påkalla hitta minsta värdet funktionen
        omrade = omrade_val()
        prisklass = prisklass_val()
        namn = bostad_val()
        year = year_choice()
        kolumn = kolumn_logic(omrade,prisklass)
        minsta,manad = minsta_ekv(namn,year,kolumn)
        print(f"\nPriset på el under {year} var som lägst under {manad} på {minsta} öre / Kwh")
        break
    elif user_choice_menu == "6": #Om användaren skriver ""6 så kommer de att påkalla analys funktionen
        namn = bostad_val()
        if namn == lgh:           #denna del gör att användare få se vilket bostadstyp de valde tidigare
            levnad = "lägenheter"
        elif namn == villa:
            levnad = "Villor"
        year = year_choice()
        analys(namn,year,levnad)
        break
    elif user_choice_menu == "7": #Om användaren skriver "7" så kommer de att avsluta loppen
        print("Program avslutas")
        break
    else:  #Om användaren skriver något annat så kommer de få möjlighet att försöka  igen
        print("\nOgiltigt värde, försök igen")