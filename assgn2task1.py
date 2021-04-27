'''
Author: Mohan 19493389
pledge of honour:I pledge by honour that this program is solely my own work.
Description: This program determines if a supermarket customer qualifies for bulk-buying discount on a product.
'''
total_grades = int(input('How many grades do you want to enter?:'))#user input value will be stored in variable "total_grades"
while total_grades < 1: #while condition for error checking,asks user to give input again if it's less than 1
    total_grades = int(input('Invalid input. Number of grades should be greater than 1. Please enter again:'))
student_marks = [] #this is a list in which values will be stored
for k in range(total_grades): #for loop for entering grades
    grades = int(input('Enter the Grade:')) #entered grades will be stored in "grades"
    student_marks.append(grades) #the stored value will be added to list "student_marks"
print('\nDisplay all grades:','\nS.No     Grades','\n----------------') #used on print command for three different outputs by using \n
template = '{0:<10}{1:<10}' # formatting output
serial_number = 0 #initially assigned to 0 and increments in below for loop
add = 0 # this add variable will be used to calculate average later
for k in student_marks: #for loop for printing output and calculating sum(add)
    serial_number=serial_number+1
    add = add + k
    print(template.format(serial_number,k))
print('\nCalculate the Average:')    
avg = add/total_grades #average formula
print('Average grade:','{0:>10.2f}'.format(avg)) 
