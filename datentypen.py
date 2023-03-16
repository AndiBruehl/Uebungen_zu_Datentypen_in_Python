# String und Integer mit Konvertierung

txt = 'ist das langweilig gerade'
print(txt)

x:int = 5
y:float = 7.34
sum = x + y
print(sum)
print(type(txt))
print(type(x))
print(type(y))
print(type(sum))

x = "Danke das hat Spass gemacht"
print(x)
print(type(x))

# Boolsche Werte


wert1 = 10
wert2 = 23
if (wert1 > wert2):
    print ("wert1 ist größer als wert2")
else:
    print ("wert1 ist kleiner als wert2")

isLoggedIn = True

if(isLoggedIn):
    print("Nutzer ist eingeloggt")
else:
    print("Nutzer ist nicht eingeloggt")
print("")
Gaeste = 33
VegiDabei = True
mercimek = ["Zwiebeln", "Öl", "Tomatenpaste", "rote Linsen", "Kartoffeln", "Minze"]
print(type(mercimek))
print(mercimek)
mercimek.append("Paprikapulver")
print(mercimek[0])
print(mercimek[4])
print(mercimek[3])

print("")
print ("Anzahl der Zutaten: "  + str(len(mercimek)))
print("")

for zutat in mercimek:
    print (zutat)
print("")

krimskrams = {"Knöpfe", "Aufnäher", "Stifte"}
print(type(krimskrams))
for zeugs in krimskrams:
    print(zeugs)

Gruppe = ("Anja", "Andi", "Basti")
print(type(Gruppe))
for Teilnehmer in Gruppe:
    print(Teilnehmer)

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

text = ["Python", "ist", "gar", "nicht", "so", "schwer", ":-)"]
print(type(text))
for wort in text:
    print(wort)