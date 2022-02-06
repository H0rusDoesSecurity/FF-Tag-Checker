
print(" _____           _____ _               _             ")
print("|_   _|         /  __ | |             | |            ")
print("  | | __ _  __ _| /  \| |__   ___  ___| | _____ _ __ ")
print("  | |/ _` |/ _` | |   | '_ \ / _ \/ __| |/ / _ | '__|")
print("  | | (_| | (_| | \__/| | | |  __| (__|   |  __| |   ")
print("  \_/\__,_|\__, |\____|_| |_|\___|\___|_|\_\___|_|   ")
print("            __/ |                                    ")                             
print("  v0.1.2   |___/                by H0rus             ")                            
print("=====================================================")

# kurze Tags setzen
italic = '!!i'
bold = '!!b'
underline = '!!u'
linethrough = '!!l'
closestyle = '/!!'

center = '??c'
left = '??l'
right = '??r'
closealign = '/??'

inp = open("inp.txt", "r")
outp = open("outp.txt", "w")
for num, line in enumerate(inp, 1):
    # öffnende und schließende tags záhlen
    style = line.count(italic)+ line.count(bold) + line.count(underline) + line.count(linethrough) - line.count(closestyle)
    if (style > 0):
        print ("Zeile ", num, ": ", style, " fehlende(r) [/style] Tag\n\t", line[0:35].strip('\n'), "...\n",sep='')
    if (style <0):
        print ("Zeile ", num, ": ", style*-1, " [/style] Tag(s) zu viel\n\t", zeile, ": ", line[0:35].strip('\n'), "...\n", sep='')
    align = line.count(left)+ line.count(right) + line.count(center) - line.count(closealign)
    if (align > 0):
        print ("Zeile ", num, ": ",align, " fehlende(r) [/align] Tag\n\t", line[0:35].strip('\n'), "...\n", sep='')
    if (align < 0):
        print ("Zeile ", num, ": ",align*-1, " [/align] Tag(s) zu viel\n\t", line[0:35].strip('\n'), "...\n", sep='')
    # ersetzen
    line = line.replace(italic, "[style type=\"italic\"]")
    line = line.replace(bold, "[style type=\"bold\"]")
    line = line.replace(underline, "[style type=\"underlined\"]")
    line = line.replace(linethrough, "[style type=\"linethrough\"]")
    line = line.replace(closestyle, "[/style]")
    line = line.replace(left, "[align type=\"left\"]")
    line = line.replace(right, "[align type=\"right\"]")
    line = line.replace(center, "[align type=\"center\"]")
    line = line.replace(closealign, "[/align]")
    outp.write(line)
inp.close()
outp.close()
input("Fertig!")
