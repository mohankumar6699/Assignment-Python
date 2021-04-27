'''
Author: Mohan 19493389
pledge of honour:I pledge by honour that this program is solely my own work.
Description: This program determines if a supermarket customer qualifies for bulk-buying discount on a product.
'''
from datetime import datetime 
def read_data(supermarket_data): #created a function to read data from "supermarket_data.txt". This will be used in main() function
    records = [] # creating a list to store data
    with open('supermarket_data.txt', 'r') as supermarket_readfile: #with as statement is used to avoid closing file object manually
        for line in supermarket_readfile: #for loop to read everyline in the text file
            line = line.strip()
            a_list = line.split(",") #splits the line into list
            date = datetime.strptime(a_list[0], "%d-%m-%Y")
            branch_name= a_list[1]  #extract name as string
            total_daily_sale = float(a_list[2]) 
            daily_transactions = int(a_list[3]) 
            rec = [date, branch_name, total_daily_sale, daily_transactions] #list items will be stored in "rec"
            records.append(rec) #"rec" data will be appended "records" list
    return records
def print_all_records(records): #created a function to print records. This will be used in main() function
    head_temp = '{0:<20}{1:<25}{2:<25}{3:<35}' #heading formatting
    print('*********************printing all records*********************') 
    heading = head_temp.format("Date", "Branch", "Daily Sale",  "Transactions")
    print(heading)
    print('-'*80) #"-" this symbol will be printed 80 times
    row_temp = '{0:<20}{1:<25}${2:<25}{3:<35}' #row formatting
    for rec in records: #for loop to print list records
        date = rec[0].strftime('%d-%m-%Y') #extracting date and converting from string to object
        branch_name = rec[1]
        total_daily_sale = float(rec[2])
        daily_transactions = int(rec[3])
        row = row_temp.format(date, branch_name, total_daily_sale, daily_transactions)
        print (row)
       
def query_branch_sale(records): #created a function to search for records using branch name. This will be used in main() function
    total_sale = 0
    total_transactions = 0
    count = 0
    print("***********************Querying total sales by branch************************")
    branch = input('Please enter the branch name: ')
    rec_found = 0
    for rec in records: #for loop for calculating total sale, total transactions and count
        if rec[1].lower() == branch.lower():
            rec_found = 1
            total_sale+=rec[2]
            total_transactions +=rec[3]
            count+=1
           
    if rec_found == 0: #if condition for no records found and following outputs will be printed, else correct records and following outputs will be printed.
        print('Total sale by', branch,"$0")
        print('Average sale by',branch,"$0")
        print('Total transactions by',branch,"0")
        print('Average number of transactions per day by',branch,"0")  
    else:
        print("Total sale by branch $",total_sale)  
        print("Average sale by branch $",total_sale/count)
        print("Total transactions by branch ",total_transactions)
        print("Average number of transactions per day by branch ",total_transactions/count)
               
def query_record_by_date(records): #function for searching records by date. This will be used in main() function
    temp = '{0:<20}{1:<25}${2:<25}{3:<35}' #formatting the output
    print("**********************Querying a Record by Date****************************")
    datestr = input('Enter a date(dd mm yyyy): ')
    date = datetime.strptime(datestr, '%d %m %Y') #date converts to object
    rec_found = None
    for rec in records: #for loop for records search
        if rec[0] == date:
            rec_found = rec
            break
    if rec_found == None: #no records will be printed
        print('No record found for date:',datestr)
    else: #records will be printed with below formatting
        print(temp.format(datestr,rec_found[1], rec_found[2],rec_found[3]))
        print ('ATV for the day: {0:.2f}'.format(rec_found[2]/rec_found[3]))

def query_period_sales(records): #function to search for sales for a particular time period
    print("********************Querying Sales Between Two Dates*************************")
    first_date = input('Enter start date(dd mm yyyy): ')
    last_date = input('Enter end date(dd mm yyyy): ')
    total_sale = 0
    date_start = datetime.strptime(first_date, '%d %m %Y')
    date_end = datetime.strptime(last_date, '%d %m %Y')
    for rec in records:
        if rec[0]>=date_start and rec[0]<=date_end:
            total_sale += rec[2]
    else:      
        print('Total sale between',first_date,'and',last_date, 'is: $',total_sale)
           
def write_data(backup,records): #function to backup the data and it will be stored in a backup file "backup.txt"
    with open('backup.txt', 'w') as writefile:
        for rec in records:
            date =rec[0].strftime("%d-%m-%Y")
           
            branch = str(rec[1])
            daily_sale = str(rec[2])
            transactions = str(rec[3])
            new_rec =[date,branch, daily_sale, transactions]
            line = ','.join(new_rec)
            writefile.write(line + "\n")
           
def main(): #main fuction and all the previous functions will be used here to get output
    records = read_data('supermarket_data.txt')
    print_all_records(records)
    query_branch_sale(records)
    query_record_by_date(records)
    query_period_sales(records)
    write_data('backup.txt',records)
main()
