import math
from collections import namedtuple
import time





def main():
    print("Enter 1 for Income Calculator.")
    print("Enter 2 for SNAP/EBT resources.")
    print("Enter 3 for housing resources.")
    print("Enter 4 for team credits.")
    user_input = int(input())
    if user_input == 1:
        calculator()
    elif user_input == 2:
        snap_links()
    elif user_input == 3:
        housing_links()
    elif user_input == 4:
        credits()
    else:
        print("Please enter valid input.")
        time.sleep(2)
        main()
        
def calculator():
    #SNAP monthly REQ 
    SNAP_REQ = (2608, 3525, 4442, 5358, 6275, 7192)
    #minimum amount of hours
    HOURS_MIN = 80
    #federal req
    FEDERAL_REQ = (31920, 43280, 54640, 66000, 76720, 88720, 100080, 111440)
    #FEDERAL MIN HOURS
    FEDERAL_HOURS_MIN = 80

    # snap req
    snap = namedtuple("snap", ["income", "hours", "state", "people"])
    #Federeal named tuple requirement
    fed = namedtuple("fed", ["income", "hours", "people"])


    print("These questions are to check washingtons monthly income")
    time.sleep(2)
    snap = snap(int(input("What is the households monthly income? ")), int(input("What are the hours you have worked in the past month? ")), input("Do you live in washington (yes or no)? "), int(input("How many people are in the household? ")))
    print("These questions are to check the federal income")
    time.sleep(2)
    fed = fed(int(input("What is the households yearly income? ")), int(input("What are the hours you have worked in the past month? ")), int(input("How many people are in the household? ")))
    #calculate income and return True or False
    def income_calc():
        if snap.people <= 6:
            if snap.income <= SNAP_REQ[snap.people - 1]:
                return True
            else:
                return False
        elif snap.people > 6:
            if snap.income <= SNAP_REQ[-1] + (snap.people * 917):
                return True
            else:
                return False



    #calculate if they work enough hours
    def hours_worked_calc():
        if snap.hours >= HOURS_MIN:
            return True
        else:
            return False
    
    #see whether they live in washington or not
    def live_in_washington():
        x = str(snap.state)
        if x == "yes":
           return True
        else:
            return False

    #collect all calculations and see if they qualify for snap
    def snap_qual():
        if income_calc() == True and hours_worked_calc() == True and live_in_washington() == True:
            print("You qualify based on Washingtons monthly.")
        else:
            print("you dont qualify based on Washingtons monthly.")
            print()
    #print out why they didnt qualify
            print(f"Qualified income: {income_calc()}")
            print(f"Qualified hours: {hours_worked_calc()}")
            print(f"Live in washington: {live_in_washington()}")
    '''
    ######
    ######
     ######
    '''
    # federal calculator
    def fed_calc():
        if fed.people <= 8:
            if fed.income <= FEDERAL_REQ[fed.people - 1]:
                return True
            else:
                return False
        elif fed.people > 6:
            if fed.income <= SNAP_REQ[-1] + (snap.people * 5680):
                return True
            else:
                return False

#fed hour calc
    def fed_hours_worked_calc():
        if fed.hours >= FEDERAL_HOURS_MIN:
            return True
        else:
         return False
    #check if they qualify for federal
    def federal_qual():
        if fed_calc() == True and fed_hours_worked_calc() == True:
            print("You Qualify based on Federal yearly.")
        else:
            print("you dont qualify based on Federal yearly.")
            print()
            #print why you dont qualify
            print(f"Qualified income: {fed_calc()}")
            print(f"Qualified hours: {fed_hours_worked_calc()}")


    #Program
    income_calc()
    hours_worked_calc()
    snap_qual()
    #Federal Program
    fed_calc()
    fed_hours_worked_calc()
    federal_qual()
    time.sleep(3)
    user_input = input("Would you like to return to the main menu? Y/N: ")
    if user_input == "Y" or user_input == "y":
       main()
    else:
        pass
def snap_links():
    print("---- How to Apply for Basic Food Benefits ----" )
    print("1. Apply online at https://www.washingtonconnection.org")
    print("2. By phone by calling 877-501-2233.")
    print("3. In person at your local DSHS Community Services Office.\n   Find a CSO near you at www.dshs.wa.gov/office-locations")
    print("4. By mail: Send your application to:")
    print("   DSHS Customer Service Center")
    print("   P.O. Box 11699, Tacoma, WA 98411-6699.")
    print("   For more information about the mailing, call 877-501-2233.")
    print("---- Additional links that can help you apply for EBT ----")
    print(" https://www.washingtonconnection.org/home")
    print(" https://www.usa.gov/food-stampsLinks to an external site.")
    time.sleep(4)
    print()
    user_input = input("Would you like to return to the main menu? Y/N: ")
    if user_input == "Y" or user_input == "y":
        main()
    else:
        pass
def housing_links():
    print("---- Affordable Housing Resources ----")
    print("General Affordable Housing: ")
    print(" Apply online at https://www.housinghope.org/affordable-housing")
    print(" For Rent Support and section 8 housing use the link below:")
    print(" https://hasco.org/applicants/apply-for-housing-online")
    time.sleep(4)
    print()
    user_input = input("Would you like to return to the main menu? Y/N: ")
    if user_input == "Y" or user_input == "y":
        main()
    else:
        pass
def credits():
    print("Alex Garcia - Income Calculator")
    print("Duy Tran - Planning, presentaion management")
    print("Diego Hernandez Saldana - Links to resources for SNAP and housing")
    print("Tyler Ivester - Main menu and module navigation ")
    time.sleep(4)
    print()
    user_input = input("Would you like to return to the main menu? Y/N: ")
    if user_input == "Y" or user_input == "y":
        main()
    else:
        pass

main()