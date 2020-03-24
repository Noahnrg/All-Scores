def adjustDate(date,change):
    currentDay = int(str(date)[6:])
    leftOverDays = (currentDay + change)
    if leftOverDays <= 0:
        cmDays = getMonthDays(int(date[4:6])-1)
        print("Last month has",cmDays,"days")
        newDate = date[0:4] + changeMonth(date[4:6]) + str(int(cmDays) + leftOverDays )                  
    else:
        newDate = (int(date)+(int(change)))

    a = """print("The date is",date)
    print("The change is",change)
    print("The new date is",newDate)"""
    return str(newDate)
    
def getMonthDays(monthNum):
        a = {1:31,2:28,3:31,4:30,5:31
            ,6:30,7:31,8:31,9:30,
            10:31,11:30,12:31}
        return str(a[monthNum])

def changeMonth(month):
    if int(month) == 1:
        return str(12)
    else:
        if int(month) - 1 <= 9:
            return "0" + str((int(month) - 1)/1)
        else:
            return str(int(month) - 1)
        
def searchForDate(inputString):
    if "tomorrow" in inputString:
        return 1
    elif "yesterday" in inputString:
        return -1
    elif "days" in inputString:
        stringList = inputString.split(" days")
        w = stringList[0].split(" ")
        k = len(w)
        if stringList[1].lower() == " ago":
            return -int(w[k-1])
        else:
            return int(w[k-1])
    elif "week" in inputString:
        stringList = inputString.split(" week")
        w = stringList[0].split(" ")
        k = len(w)
        mult = 1
        if w[k-1].lower() in ["a","next"]:
            mult = 1
        elif "last" == w[k-1].lower():
            mult = -1
        else:
            mult = int(w[k-1])
            
        if "ago" in inputString:
            return mult * -7
        
        else:
            return mult * 7              
    else:
        return 0

def switchTime(time):
    if time.lower().strip() == "pm":
        return "AM"
    else:
        return "PM"

def URLDateFrom(change = 0):
    from datetime import datetime
    now = datetime.now()
    day,month,year = str(now.day),str(now.month),str(now.year)
    del now
    if int(day)<10:
        day = "0"+day
    if int(month)<10:
        month = "0"+month
    return adjustDate((year+month+day),change)

def UTC2CT(timeString):
    actualTime = str(timeString.strip()).split(":")
    try:
        actualTime[0] = str(int(actualTime[0]) - 6)
    except:
        return ""

    if int(actualTime[0]) <= 0:
        actualTime[0] = str(int(actualTime[0])+12)

    if int(actualTime[0]) in range(6,12):
        actualTime[1] = (str(actualTime[1])[:2]) + switchTime(str(actualTime[1])[2:4])
        
    centralTime = actualTime[0] +":"+ actualTime[1]+ " CT" 
    return centralTime
