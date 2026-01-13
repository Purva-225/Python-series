LEARNING SERIES IS GROWING CONSISTENTLY WORKING FOR MY FUTURE PROJECT AND HERE IS IT'S BEGINNING: 


""""to cnt the len""" 

r = input("Enter your name: ")
length = len(r)
print(length)

"""if i want to print signal lights using conditions"""

r = input("ENTER SIGNAL LIGHT COLOUR: ")

if r== "red":
  print("Stop 🫷🏼🚏")

elif r== "yellow":
 print("ready/slow down🛄")
elif r == "green":
 print("Go 🥹👋🏼")
else:
    print("invalid signal")

"""grade of student"""
marks = int(input("Enter marks of student: "))
if marks >= 90:
   grade = 'A'
elif marks >= 80 and marks < 90:
      grade = 'B'
else:
    grade = 'c'
print("Grade of student: ", grade)
        
"""odd even"""
num = int(input("Enter a number: "))
if(num% 2 == 0): 
    print("EVEN num")
else:
    print("an odd")


"""greatest of 3 num entered by user"""
a = int(input("Enter the First Num: "))
b = int(input("Enter the Second Num: "))
c = int(input("Enter the Third Num: "))

if a >= b and a >= c:
  print("Greatest number is ", a)
elif b >= a and b >= c:
  print("Greatest number is ", b)
else:
  print("Greatest number is ", c)

"""WAP to ask user to enter their 3 fav movies and store in a list: """
movies = []
movie1 = input("enter your no.1 fav movies: ")
movie2 = input("enter your no.2 fav movies: ")
movie3 = input("enter your no.3 fav movies: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

"""WAP to check if a list contains palindrome of elements.(hint: use copy()method) given: [1,2,3,2,1]"""
list = [1,2,3,2,1,4]

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("Is a Palindrome")
else:
    print("Not A Palindrome")

"""WAP to cnt num of students with the 'A' grade in following tuple. ["a","a","c","d","f","f","e"]"""

grade = ["a","a","c","d","f","f","e"]
print(grade.count("e"))

grade = ["a","a","c","d","f","f","e"] 
grade.sort()
print(grade)
