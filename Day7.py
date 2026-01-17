"""file I/O """
#in r+ mode file does not truncate and it is used for read and write the data. 
f = open("sample.txt","r+") #Overwrite's
f.write("poorie")
print(f.read()) #reads content present in file 
f.close()

"""To create an file if already not created"""
f = open("sample.txt", "a")
f.close()

f = open("sample.txt", "w")
f.close()

# w+ allows for reading and writing but it will truncate 
f = open("sample.txt","w+") 
#f.write("poorie")
print(f.read()) #reads content present in file 
f.write("poorie")
f.close()

#SUMMARY 
# r+ = read + overwrite (pointer starts from starting) NO TRUNCATE 
# w+ = read + overwrite ,  TRUNCATE 
# a+ = read and append , NO truncate 

"""With fun"""
with open("sample.txt","r") as f:
    data = f.read()
    print(data)

with open("sample.txt","w") as f:
   f.write("Poorie sweet")


"""Deleting a file"""
# using the os module (Deleting file)
#import os
#os.remove("doc.txt")

"""Create a file using py and add the txt"""
f = open("Practice.txt", "a")
f.close()
