def condition_check(year):#To check the year between 1800 to 2200
    if year>=1800 and year<1900:
        oper=operations1800(day,c,rem)
        return(oper)
    elif year>=1900 and year<2000:
        oper=operations1900(day,c,rem)
        return(oper)
    elif year>=2000 and year<2100:
        oper=operations2000(day,c,rem)
        return(oper)
    elif year>=2100 and year<2200:
        oper=operations2100(day,c,rem)
        return(oper)
    else:
        print("Please enter the year between 1800-2100")
        print("Because my creater invented me as to find only 1800-2100 centuries")
def last(year):#To cut the last two value of the year
    d1=int(year%10)
    d2=int(year/10)
    d3=int(d2%10)
    ltwo=int(((d3*10)+d1))
    return (ltwo)
def fifty_percent(two_number,):#to get the credit value
    f=int(two_number/2)
    tf=int(f/2)
    credit=int(two_number+tf)
    dcredit=(credit/7)
    mod_credit=int(credit%7)#print("Mod of the credit ",mod_credit)
    return(mod_credit)
def code(month):
    if month==1:
        return(6)
    elif month==2:
        return(2)
    elif month==3:
        return(2)
    elif month==4:
        return(5)
    elif month==5:
        return(0)
    elif month==6:
        return(3)
    elif month==7:
        return(5)
    elif month==8:
        return(1)
    elif month==9:
        return(4)
    elif month==10:
        return(6)
    elif month==11:
        return(2)
    elif month==12:
        return(4)
def leap_year_code(month):
    if month==1:
        return(5)
    elif month==2:
        return(1)
    elif month==3:
        return(2)
    elif month==4:
        return(5)
    elif month==5:
        return(0)
    elif month==6:
        return(3)
    elif month==7:
        return(5)
    elif month==8:
        return(1)
    elif month==9:
        return(4)
    elif month==10:
        return(6)
    elif month==11:
        return(2)
    elif month==12:
        return(4)
def operations1800(day,c,rem):#do the work for 1800
    first=(day+c+rem+3)
    second=int((first/7))
    third=int((first%7))
    return(third)
def operations1900(day,c,rem):#do the work for 1900
    first=(day+c+rem+1)
    second=int((first/7))
    third=int((first%7))
    return(third)
def operations2000(day,c,rem):#do the work for 2000
    first=(day+c+rem)
    second=int((first/7))
    third=int((first%7))
    return(third)
def operations2100(day,c,rem):#do the work for 2100
    first=(day+c+rem+5)
    second=int((first/7))
    third=int((first%7))
    return(third)

def CheckLeap(year): #check is it leap year   
  if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):   
    print("The given Year is :Leap Year")
    return(1)
  else:  
    print("The given Year is :Not a Leap Year")
    return(0)
def error():#if any error pre defined user output
    print("This is not the proper date")
    print("The day,month and year should be in the numberical form")
    print("EX: 1/1/2022")
    print("The day of the any month are in below 31")
    print("The month of the any year are in 12 ")
    print("SO PRINT IT PROPERLY")
def week(oper):#given
    if oper==1:
        print("The given Day is  :MONDAY")
    elif oper==2:
        print("The given Day is  :TUESDAY")
    elif oper==3:
        print("The given Day is  :WEDNESDAY")
    elif oper==4:
        print("The given Day is  :THURSDAY")
    elif oper==5:
        print("The given Day is  :FRIDAY")
    elif oper==6:
        print("The given Day is  :SATURDAY")
    elif oper==7:
        print("The given Day is  :SUNDAY")
    elif oper==0:
        print("SUNDAY")
print("----------------------------------------------------------------------------------")
print("      //GIVE ME THE EXACT DATE I WILL TELL YOU WHAT IS THE DAY OF THE DATE//")
print("                             //IS LEAP YEAR OR NOT//")
print("                              //BETWEEN 1800-2200//")
print("----------------------------------------------------------------------------------")
print("NOTE:")
print("    The format of the date is :01/05/2073\n\n\n")  
day,month,year=map(int,input("Enter the date    :").split("/"))
if day>0 and day<=31 and month>=1 and month<=12:
    if month ==2 and day == 30:
        error()
    elif month ==4 and day==31:
        error()
    elif month== 6 and day==31:
        error()
    elif month==9 and day==31:
        error()
    elif month==11 and day==31:
        error()
    else:
        leap_year=CheckLeap(year)
        if leap_year==1:
            two_number=last(year)
            rem=fifty_percent(two_number)
            c=leap_year_code(month)
            oper=condition_check(year)
            week(oper)
        else:
            if month == 2 and day == 29:
                error()
            else:
                two_number=last(year)
                rem=fifty_percent(two_number)
                c=code(month)
                oper=condition_check(year)
                week(oper)
else:
    error()
print("-------------------------------------------------------------------------------------")



