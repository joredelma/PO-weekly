lowwer = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
comp = {}
comp2 = {}
for y in range(len(lowwer)):
    comp[lowwer[y]]=y
    comp2[y]=lowwer[y]
def Atbash(str):
    newstr = ""
    for x in range(len(str)):
        if str[x] == " ":
            newstr.append(" ")
        if str[x] in lowwer:
            newstr = newstr + comp2[25 - comp[str[x]]]
        if str[x] in upper:
            newstr = newstr + comp2[25 - comp[str[x].lower()]].upper()
    return newstr
print(Atbash("zyx"))

    