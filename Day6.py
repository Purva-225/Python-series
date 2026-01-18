"""OOP"""

class Student:
    name = "Poorva"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

"""Example: """

class Car:
    color = "Black"
    Brand = "mercedes"

car1 = Car() 
print(car1.color)
print(car1.Brand)

"""Constructor = --init--"""
"""SELF PARAMETER"""

#self parameter is the  reference to the current instance of class, and used to acess variables that belongs to class. 
#the data we store inside the class or object as variable,data is:
#known as: ATTRIBUTES

class Student :

    def __init__(self, name, marks):
       self.name = name
       self.marks = marks
       print("Adding new students data...")

s1 = Student("Poorie",44)
print(s1.name, s1.marks)

s2 = Student("Hit",98)
print(s2.name, s2.marks)

"""Default Construvtor"""
class Student:
    def __init__(self):
        pass

    #Parameterized Constructor
    #jiske andr self ke alawa bhi parameters hote hai
def __init__(self,marks,name):
        self.name = name
        self.marks = marks
        print("something")

class Student: 
    """Attribute and its types: """
college_name = "avjsd"
    #below are two types of attribute 
    #class.attr 
    #obj.attr
    #jab bhi obj attribute our class attribute ki same value hoti hai usmai 
    #sabse jyada prefrence Object attribute obj.attr ko dena hai.
def __init__(self,marks,name):
        self.name = name
        self.marks = marks
        
def welcome(self):
      print("welcome student, ",self.name)

def get_marks(self):
      return self.marks

s1 = Student("Poorie",98)
s1.welcome()
print(s1.get_marks())

 """create student class that takes name & marks of 
3 subj as arguments in constructor.
then create a method to print the avg"""
class Student:
  def __init__(self,name,marks):
            self.name = name
            self.marks = marks

  def get_avg(self):
    sum = 0
    for val in self.marks:
         sum += val
    print("hi", self.name, "your avg marks are:", sum/3)
         
s1 = Student("poorie,",[99,88.77])
s1.get_avg()


"""create acc class with 2 attributes - balance and acc no. 
create methods for debit,credit and printing bal"""

class Account:
    def __init__(self, acc, bal):
        self.balance = bal
        self.account_no = acc

    # Adding methods
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance to debit Rs.", amount)
        else:
            self.balance -= amount
            print("Rs.", amount, "was debited")
            print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 225)
acc1.debit(700000)  
acc1.credit(4000)
acc1.credit(23)

