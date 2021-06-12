print(" _____           _____ _               _             ")
print("|_   _|         /  __ | |             | |            ")
print("  | | __ _  __ _| /  \| |__   ___  ___| | _____ _ __ ")
print("  | |/ _` |/ _` | |   | '_ \ / _ \/ __| |/ / _ | '__|")
print("  | | (_| | (_| | \__/| | | |  __| (__|   |  __| |   ")
print("  \_/\__,_|\__, |\____|_| |_|\___|\___|_|\_\___|_|   ")
print("            __/ |                                    ")                             
print("  v0.1     |___/                by H0rus/WeilIchsKann")                            
run=True
while run==True:
    print("=====================================================")
    inp = open("inp.txt", "r")
    outp = open("outp.txt", "w")
    style = 0
    align = 0
    zeile = 1
    for line in inp:
        a = line
        style = a.count("!!i")+ a.count("!!b") + a.count("!!u") + a.count("!!l") - a.count("/!!")
        if (style > 0):
            print ("Zeile ", zeile, ": ", style, " fehlende(r) [/style] Tag\n\t", a[0:35].strip('\n'), "...\n",sep='')
        if (style <0):
            print ("Zeile ", zeile, ": ", style*-1, " [/style] Tag(s) zu viel\n\t", zeile, ": ", a[0:35].strip('\n'), "...\n", sep='')
        align = a.count("??l")+ a.count("??r") + a.count("??c") - a.count("/??")
        if (align > 0):
            print ("Zeile ", zeile, ": ",align, " fehlende(r) [/align] Tag\n\t", a[0:35].strip('\n'), "...\n", sep='')
        if (align < 0):
            print ("Zeile ", zeile, ": ",align*-1, " [/align] Tag(s) zu viel\n\t", a[0:35].strip('\n'), "...\n", sep='')
        a = a.replace("!!i", "[style type=\"italic\"]")
        a = a.replace("!!b", "[style type=\"bold\"]")
        a = a.replace("!!u", "[style type=\"underlined\"]")
        a = a.replace("!!l", "[style type=\"linethrough\"]")
        a = a.replace("/!!", "[/style]")
        a = a.replace("??l", "[align type=\"left\"]")
        a = a.replace("??r", "[align type=\"right\"]")
        a = a.replace("??c", "[align type=\"center\"]")
        a = a.replace("/??", "[/align]")
        outp.write(a)
        style = 0
        align = 0
        zeile+=1
    inp.close()
    outp.close()
    print("Fertig!")
    print("Falls es Fehler gab und du sie behoben hast, kann ich inp.txt erneut prüfen\n\t 'y' = ja\n\tAndere Eingabe = nein")
    cont = input()
    if (cont !='y' or 'Y'):
        run=False
            
print ("Bye!")
input()
