my_file = open("names.txt", "a+")

#my_file.write("moshe\n")


#for i in range(100):
 #   my_file.write("moshe\n")
#my_file.close()
#f1 input from user and save in file
# f2 read from file and write hello line

def get_name():
    m = input("enter a name: ")
    if m != "0" :
        my_file.write(m + "\n")
        my_file.close()

#m = get_name()
#while m != 0:
 #   m = get_name()



my_file = open("names.txt", "r")

for line in my_file.readlines():
    print(line)

with open("names.txt") as my_file:
    for line in my_file.readlines():
        print(line)




