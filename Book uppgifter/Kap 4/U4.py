Kolumner = int(input("Hur många kolumner har din multiplikationstabell? "))
Rader = int(input("Hur många rader har din multiplikationstabell? "))

List_Kolumns = []
List_Rader = []

for i in range(1, Kolumner+1):
    List_Kolumns.append(i)
for i in range(1, Rader+1):
    List_Rader.append(i)

for Rad in List_Rader:
    print("\n")
    for Kolumn in List_Kolumns:
        print(f"{Rad*Kolumn} ", end='')