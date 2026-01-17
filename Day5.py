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
with open("Practice.txt", "r") as f:
    data = f.read()

New_data = data.replace("java", "python")
print(New_data)

with open("Practice.txt", "w") as f:
    f.write(New_data)

"""Search if the word learning exist in it or not"""

word = "Tech"
with open("Practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("FOUND")
    else: 
        print("NOT FOUND")
"""WAF on which line does learning word occurs first, print -1 if not found"""

def check_for_word():
    word = "learning"
    data = True
    line_no = 1
    with open("Practice.txt", "r") as f:
       while data:
         data = f.readline()
         if(word in data):
             print(line_no)
             line_no += 1 

check_for_word()

"""from the file nums separated by comma, print the even num"""
count = 0
with open("PracticeEven.txt", "r") as f:
      data = f.read()
      print(data)

      """num = ""
      for i in range(len(data)):
       if(data[i] == ","):
          print(num) 
          num = ""
       else:
        num += data[i]"""
      
      nums = data.split(",")
      for val in nums:
            if(int(val)%2 == 0):
                  count += 1

print(count)

