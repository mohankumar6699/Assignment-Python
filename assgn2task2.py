'''
Author: Mohan 19493389
pledge of honour:I pledge by honour that this program is solely my own work.
Description: This program determines if a supermarket customer qualifies for bulk-buying discount on a product.
'''
def calc_average_enrolment(records): #created a function to calculate average enrolments. This will be used in main function
    total = 0 #initially given value "0"
    for k in records: #for loop for iterating "total"
        total = total + k[2] # enrolled students is stored in k[2]. so this will be added to "total"     
    average = total / len(records) #average formula
    print('Total:',total) 
    print('Average:',average)
    print('Done \n\n')
def print_all(records): #created a function to print values. This will be used in main() function
    heading_temp = '{0:<15}{1:<15}{2:>20}' #formatting for heading
    heading = heading_temp.format('CID','NAME','ENROLMENTS') 
    print(heading)
    print('-'*50) #"-" this symbol will be printed 50 times in horizontal direction
    format_temp = '{0:<15}{1:<15}{2:>15}' #formatting records 
    for rec in records: #for loop to print records
        row = format_temp.format(rec[0],rec[1],rec[2])
        print(row)
    print('Done.\n\n')
def search_by_courseid(records): #created a function to enable user to search records by using courseid. This will be used in main() function
    search_course = input('Please enter the courseID:') #user input will be stored in "search_course"
    format_temp = '{0:<15}{1:<15}{2:>15}' 
    available_records = None #initially avalable_records is given "none"
    for rec in records: #for loop for finding record if user input is exists
        if rec[0].lower() == search_course.lower():
            available_records = rec
            break
    if available_records == None: #this condition is used to print output based on correct/wrong input from user
        print('No record found for', search_course)
    else:
        print(format_temp.format(available_records[0], available_records[1], available_records[2]))
    print('Done.\n\n')
def getdata(): #this function is used to create a list and storing data in the list
    course_list = [] #below records will be stored in this list
    course_list.append(['comp001','Fundamentals',135]) #data that goes into list "course_list"
    course_list.append(['comp002','Intro Database',30]) #data that goes into list "course_list"
    course_list.append(['comp003','Web Progarmming',24]) #data that goes into list "course_list"
    return course_list
def main(): #this is the main fucntion and all previous fuctions will be called from here.
    data = getdata()
    print_all(data)
    calc_average_enrolment(data)
    search_by_courseid(data)
   
main() 