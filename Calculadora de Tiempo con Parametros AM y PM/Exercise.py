def add_time(startTime, durationTime, newDay=""):
    amountDays = 0
    if len(startTime) > 7:
        initialHour = startTime[0:2]
        initialMinutes = startTime[3:6]
    else:
        initialHour = startTime[0:1]
        initialMinutes = startTime[2:5]
    if len(durationTime) > 4:
        hoursPassed = durationTime.split(":")[0]
        minutesPassed = durationTime.split(":")[1]
    else:
        hoursPassed = durationTime[0:1]
        minutesPassed = durationTime[2:5]
    newHour = int(initialHour) + int(hoursPassed)
    newMinute = int(initialMinutes) + int(minutesPassed)

    if newDay.lower() == "monday" or newDay == "":
        numberDay = 0
    elif newDay.lower() == "tuesday":
        numberDay = 1
    elif newDay.lower() == "wednesday":
        numberDay = 2
    elif newDay.lower() == "thursday":
        numberDay = 3
    elif newDay.lower() == "friday":
        numberDay = 4
    elif newDay.lower() == "saturday":
        numberDay = 5
    elif newDay.lower() == "sunday":
        numberDay = 6

    while newMinute >= 60:
        newHour += 1
        newMinute = newMinute - 60
    if startTime[6:8] == "AM" or startTime[5:7] == "AM":
        repeatOnce = 0
        value = " AM"
        while newHour >= 13:
            newHour = newHour - 12
            numberDay += 0.5
            amountDays += 0.5
            if value == " AM":
                value = " PM"
            else:
                value = " AM"
            if numberDay == 7 and newDay != "":
                numberDay -= 7
        if numberDay <= 0.5 and newHour == 12 and repeatOnce == 0:
            value = " PM"
            repeatOnce += 1
        elif numberDay > 0.5 and newHour == 12 and repeatOnce > 0:
            value = " PM"
            numberDay += 1
    else:
        value = " PM"
        numberDay += 0.5
        amountDays += 0.5
        while newHour >= 13:
            newHour = newHour - 12
            numberDay += 0.5
            amountDays += 0.5
            if numberDay == 7.0 and newDay != "":
                numberDay = numberDay - 7
            if value == " PM":
                value = " AM"
            else:
                if newHour == 12:
                    value = " AM"
                else:
                    value = " PM"
        if newHour == 12:
            value = " AM"
            numberDay += 1
            amountDays += 1

    exactMinute = str(newMinute)
    if newMinute < 10:
        exactMinute = "0" + exactMinute

    if newDay == "" and numberDay < 1:
        return str(newHour) + ":" + exactMinute + value
    elif newDay == "" and 1 <= numberDay < 2:
        newDay = "(next day)"
        return str(newHour) + ":" + exactMinute + value + " " + newDay
    elif newDay == "" and numberDay >= 2:
        numberDay = int(numberDay)
        newDay = "(" + str(numberDay) + " days later)"
        return str(newHour) + ":" + exactMinute + value + " " + newDay

    elif newDay != "" and numberDay < 1:
        newDay = "Monday"
    elif newDay != "" and 1 <= numberDay < 2:
        newDay = "Tuesday"
    elif newDay != "" and 2 <= numberDay < 3:
        newDay = "Wednesday"
    elif newDay != "" and 3 <= numberDay < 4:
        newDay = "Thursday"
    elif newDay != "" and 4 <= numberDay < 5:
        newDay = "Friday"
    elif newDay != "" and 5 <= numberDay < 6:
        newDay = "Saturday"
    elif newDay != "" and 6 <= numberDay < 7:
        newDay = "Sunday"

    if amountDays < 1:
        return str(newHour) + ":" + exactMinute + value + ", " + newDay
    elif 1 <= amountDays < 2:
        return str(newHour) + ":" + exactMinute + value + ", " + newDay + " (next day)"
    elif amountDays >= 2:
        amountDays = int(amountDays)
        return str(newHour) + ":" + exactMinute + value + ", " + newDay + " (" + str(amountDays) + " days later)"
print(add_time("6:30 PM", "205:12"))