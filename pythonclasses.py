class Person:
	def __init__(self,fname: str,lname: str):
		self.firstname = fname 
		self.lastname = lname 

	def printname(self):
		return f'Firstname : {self.firstname}, Lastname : {self.lastname}'

	def __str__(self):
		return f'{self.firstname} {self.lastname}'

class Student(Person):

	def __init__(self,fname: str,lname: str):
		Person.__init__(self,fname,lname)
	
	def __str__(self):
		return f'Welcome to Class {self.firstname} {self.lastname}'


p1 = Student("Nithin","Raj")
print(p1)