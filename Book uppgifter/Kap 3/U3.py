import math #Viktig för att enkelt kunna göra matematiska uträkningar

A_sida = float(input("Vad är sida A:s längd? "))
B_sida = float(input("Vad är sida B:s Längd? "))

Vinkel = math.radians(float(input("Vad är vinkeln mellan A och B? "))) #converterar input som jag antar kommer vara i grader till radianer innan den skickas till Vinkel

C_sida = math.sqrt((A_sida**2) + (B_sida**2) - (2*A_sida*B_sida*math.cos(Vinkel)))
Diff_AB = abs(A_sida-B_sida)
Diff_AC = abs(A_sida-C_sida)
Diff_BC = abs(B_sida-C_sida)

Tot = 10**(-10)

if (A_sida*2 - (B_sida + C_sida)) < Tot and (B_sida*2 - (A_sida + C_sida)) < Tot and (C_sida*2 - (B_sida + A_sida)) < Tot:
    print("Triangeln är liksidig. \n" \
    f"Sida C:s längd är {C_sida}")

elif (Diff_AB < 10**(-10)) or (Diff_AC < 10**(-10)) or (Diff_BC < 10**(-10)):
    print("Triangeln är likbent. \n" \
    f"Sida C:s längd är {C_sida}")

else:
    print("Triangel är oliksidig. \n" \
    f"Sida C:s längd är {C_sida}")