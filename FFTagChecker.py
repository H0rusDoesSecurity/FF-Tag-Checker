inp = open("inp.txt", "r")
outp = open("outp.txt", "w")
style = 0
align = 0
zeile = 1
for line in inp:
    a = line
    style = a.count("!!i")+ a.count("!!b") + a.count("!!u") + a.count("!!l") - a.count("/!!")
    if (style > 0):
        print (style, " fehlende(r) [/style] Tag in Zeile ", zeile, ": ", a[0:35].strip('\n'), "...\n",sep='')
    if (style <0):
        print (style*-1, " [/style] Tag(s) zu viel in Zeile ", zeile, ": ", a[0:35].strip('\n'), "...\n", sep='')
    align = a.count("??l")+ a.count("??r") + a.count("??c") - a.count("/??")
    if (align > 0):
        print (align, " fehlende(r) [/align] Tag in Zeile ", zeile, ": ", a[0:35].strip('\n'), "...\n", sep='')
    if (align < 0):
        print (align*-1, " [/align] Tag(s) zu viel in Zeile ", zeile, ": ", a[0:35].strip('\n'), "...\n", sep='')
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
    zeile = zeile + 1
inp.close()
outp.close()
print ("done")
input()
