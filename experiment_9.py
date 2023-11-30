#Write a program to implement an employee management system using classes, instances and inheritance.
# Parent class: Employee 
class Employee: 
 def __init__(self,name,employee_id): 
 self.name = name 
 self.employee_id=employee_id 
 def display_info(self): 
 print("Employee ID: ",self.employee_id) 
 print("Name: ",self.name) 
# Derived class: Manager (inherits from Employee) 
class Manager(Employee): 
 def __init__(self,name,employee_id,department): 
 super().__init__(name,employee_id) 
 self.department= department 
 def display_info(self): 
 super().display_info() 
 print("Department: ",self.department) 
# Derived class: Developer (inherits from EMployee) 
class Developer(Employee): 
 def __init__(self,name,employee_id,programming_language): 
 super().__init__(name,employee_id) 
 self.programming_language= programming_language 
 def display_info(self): 
 super().display_info() 
 print("Programming Languange: ",self.programming_language) 
# Get runtime input for Manager 
manger_name = input("Enter Manager's name: ") 
manger_id = int(input("Enter Manager's ID: ")) 
manger_department = input("Enter Manager's Department: ") 
# Get runtime input for Programer 
developer_name = input("Enter Developer's name: ") 
developer_id = int(input("Enter Developer's ID: ")) 
programing_language = input("Enter Developer's Programing Language: ") 
# Creating instances of Manager and Developers classes 
manager = Manager(manger_name,manger_id,manger_department) 
developer = Developer(developer_name,developer_id,programing_language) 
# Display information of Manger Developer 
print("\nManager Information:") 
manager.display_info() 
print("\nDeveloper Information:") 
developer.display_info() 