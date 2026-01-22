'''
Docstring for Book uppgifter.Kap 2.U1
Skriv ett program som beräknar hur många mil en bil har gått under de senaste året och bilen
genomsnittliga bensinförbrukning per mil. När programmet klrs ska det fråga efter dagen mätarställning, 
mätarstälningen för ett år sedan och hur många luter bensin som har förbrukats under året. Det ska
se ut som i följande exempel när man kör programet.

Mätarställning idag?
Mätarstälningen för ett år sedan?
Antal körda mil:
Antal liter bensin:
Förbrukning per mil:
'''
# Här kommer gur jag hade skrivigt det här programet

Mid = int(input("Mätarställning idag? "))                   #Mid är förkortning på det som står i input

Mifeas = int(input("Mätarstälningen för ett år sedan? "))   #Mifeas är förkortning på det som står i input

print(f"Antal körda mil: {Mid-Mifeas}")

Liter = int(input("Antal liter bensin: "))

literPerMil = Liter/(Mid-Mifeas)

print("Förbrukning per mil: " + str(round(literPerMil, 4)))