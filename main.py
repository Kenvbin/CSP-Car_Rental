'''
Car Rental Report
Traci Castro

Car Rental: User will be asked to enter for each customer:
  - name
  - # of miles rental car was driven
  - whether it was a premium day (Fri/Sat/Sun are premium.)
All customer info will be stored in lists

Once all customer data is entered, a report will be printed that has the following headings:
  Name 
  Miles
  Premium (an 'x' in this column indicates premium, 
           blank if non-premium) 
  Amount (see calculations below)

Each customer record will be printed with the amount calculated as follows:
  Non-Premium Days (Mon through Thurs)
    1st 50 miles-------------$3.00 per mile
    Miles after 50-----------$2.50 per mile
  Premium Days (Fri through Sun)
    1st 30 miles ------------$5.00 per mile
    Miles after 30-----------%3.25 per mile

A total will be printed after all records have been printed
'''

names=[]                #customer names
miles=[]                #number of miles driven
days=[]                 #whether rental day was premium or not
num_rentals = 0         #the number of customer records entered


def print_instructions():
  print ("Welcome to Castro's Car Rental", "\n")
  print ("You will be asked to enter the customer's name,")
  print ("the number of miles the car was driven and")
  print ("whether the car was rented on a premium day (Fri-Sun)")
  print ("or a non-premium day (Mon-Thurs).", "\n")
  go = input("Press enter to start...")
  print ("\n")
  
# enter_data collects all the customer records
def enter_data():     
  i=1
  global num_rentals
  name = input("Enter customer name (q to quit): ")
  while name != 'q':
    num_rentals += 1
    names.append(name)
    miles.append(input("Enter miles driven: "))
    days.append(input("Was it a premium day? (y/n) "))
    i += 1
    print()
    name = input("Enter customer name (q to quit): ")
  print()

# print_report prints each customer record out and at the bottom
# prints a total. 
# The parameters are:
#    day--------------the list of whether it is a premium day
#    miles_driven-----the list of number of miles driven that day
#    rentals----------the number of customer records to be printed.
#                     (this is the index for the print loop.)
# Meets AP Create Task Requirements: Function with parameter(s) 
# that affect which code is run. Function contains sequencing, 
# selection and iteration.
  
def print_report(day,miles_driven,rentals):
  
  total = 0
  i = 0
  print("Name              Miles          Prem           Amt")
  for i in range(rentals):
    if (day[i].upper() == 'N'):
      if int(miles_driven[i]) <= 50:
        fee = float(int(miles_driven[i]) * 3)
      else:
        fee =float((50 * 3) + ((int(miles_driven[i]) - 50) * 2.5))
      print ("{:<18} {:>5} {:>11} {:>15.2f}".format(names[i],int(miles[i])," ",fee))
      total += fee
    else:
      if int(miles_driven[i]) <= 30:
        fee = float(int(miles_driven[i]) * 5)
      else:
        fee = float((30 * 5) + ((int(miles_driven[i]) - 30)* 3.25))
      print ("{:<18} {:>5} {:>11} {:>15.2f}".format(names[i],int(miles[i]),"x",fee))
      total += fee
  print("{:>44} {:> 5.2f}".format( "Total", total))  
  #print(format(total," >5.2f"))

print_instructions() 
enter_data()
print_report(days,miles,num_rentals)
