try:
    a = 1/5
    #f = open("foo.txt", 'r')
#BaseException, ValueError, ZeroDivisionError and more...
except IOError:
    print("IOError: somthing wen wrong; ")
except BaseException:
    print("BaseException")
#---------
file = open("words.txt", "a+", encoding="utf-8")
file.write("טר'םקטר ר/n")
file.write("חיים/n")
file.write("הילה/n")

file.close()
#file.write("Eyal\n")
#file.write("Batya\n")
#for line in file.readlines():
#    print(line)
#file.close()