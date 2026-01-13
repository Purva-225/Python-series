# Dictionary  and setin Python


"""to store following word meaning in python dict"""
#table : "A list of furniture", list of facts and figure
#cat: A small animal 

furniture = {
     "Cat" : "A small animal",
    "table" : ["A list of furniture", "A list of facts and figure"]
    
}
print(furniture)

"""given list of sub for students,assu 1 classrm is req for 1 sub.how many classrm are needed by all std"""
Classroom = {
    " python" ,"java" ,"javascript", "c++","c" ,
     "c++", " python","java" ,"javascript",
}
print(len(Classroom))

"""WAP to enter mrk of 3 subj from user and store them in a dictionary,Start with an empty dict & add one by one. Use subj name as key & marks as val."""
marks = {}

X = int(input("Enter 1st subj mark: "))
marks.update({"phy": X})
X = int(input("Enter 2nd subj mark: "))
marks.update({"chem": X})
X = int(input("Enter 3rd subj mark: "))
marks.update({"math": X})
     
print(marks)

"""fig out a way to separate 9 and 9.0 as separate values in the set (you can take help of built in data types)"""

Data = {
    ("Float", 9.0),
    ("Int",9)
}
print(Data)

#Conpleted Dictionary & Set.
