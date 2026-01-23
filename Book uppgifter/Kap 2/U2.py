'''
Docstring for Book uppgifter.Kap 2.U2

Skriv ett program som beräknar volymen och arean av en sfär.
Som indata ges sfärens radie. Följande formler är givna:

V = (4*pi*r^3)/3        A = 4*pi*r^2
'''
import math

Radie = float(input("Vad är radien på din sfär? "))

Volym = (4*math.pi*(Radie**3))/3
Area = 4*math.pi*(Radie**2)

# .upper() gör så att programet kan aceptera både stora och små bokstäver och 
# \033[1;31;40m är för att få felmedelandet att stå ut.
while True:
    V_eller_A = str(input("\033[0;37;40m\nVill du beräkna Volym, Area eller både och? \nSkriv V för Volym, A för Area eller B för både och.\ninput: "))
    
    if V_eller_A.upper == "B":
        print(f"\nVolym = {Volym} \nArea = {Area}")
        break

    elif V_eller_A.upper() == "V":
        print(f"\nVolym = {Volym}")
        break

    elif V_eller_A.upper() == "A":
        print(f"\nArea = {Area}")
        break

    else:
        print("\033[1;31;40mDu skrev fel! Läs noga.")