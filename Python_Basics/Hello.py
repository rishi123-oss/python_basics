#Python Basics: Print and Variables

#String Variable
name= "Rishika"
course= "Computer Science"

#Number Variables
age= 18
gpa= 3.43

#Boolean Variable
is_student= True

#Printing Variables
print("Name:",name)
print("Course:",course)
print("Age:",age)
print("GPA",gpa)
print("Is_student",is_student)

#f-string printing
print(f"\nHi!My name is {name}.")
print(f"I am {age} years old and studying {course}.")
print(f"My GPA is {gpa} and student status is {is_student}.")

#Checking Variable Types
print("\n---Variable Types---")
#name:
print(type(name))
#age:
print(type(age))
#gpa:
print(type(gpa))
#is_student
print(type(is_student))

#Updating a Variable
age=21
print(f"\n Updated age: {age}")

#Multiple Assignment
x,y,z= 10, 20, 30
print(f"\nx={x},y={y},z={z}")



