kleiderschrank = ["Hose", "T-Shirt", "Kleid"]
kommode = ["Schuhe", "Socken", "Mütze"]

print("Einzelne Ausgabe:")
print("")
print(kleiderschrank[0])
print(kleiderschrank[1])
print(kleiderschrank[2])

print("")
print("")
print("Ausgabe über For-Schleife:")
print("")
for sachen in kleiderschrank:
    print(sachen)

print("")
print("")
print("Hinzufügen Pullover:")
print("")

kleiderschrank.append("Pullover")
for sachen in kleiderschrank:
    print(sachen)

print("")
print("")
print("Kommode verkauft und Sachen zum Kleidershrank hinzugefügt:")
print("")

kleiderschrank += kommode
for sachen in kleiderschrank:
    print(sachen)