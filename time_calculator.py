def add_time(start, duration,starting_day=""):

    time = start.split()
    hour = time[0].split(':')[0]
    mint = time[0].split(':')[1]
    tday = time[1]

    if tday == "PM":
        hour = str(int(hour) + 12)
        
    duration_hour = duration.split(':')[0]
    duration_mint = duration.split(':')[1]


    new_hour = int(hour) + int(duration_hour)
    new_mint = int(mint) + int(duration_mint)

    if new_mint >= 60:
        hours_add = new_mint//60
        new_mint -= hours_add*60
        new_hour += hours_add
        
    days = 0
    if new_hour > 24:
        days = new_hour//24
        new_hour -= days*24
  
    if new_hour > 0 and new_hour < 12:
        tday = "AM"
    elif new_hour == 12:
        tday = "PM"   
    elif new_hour > 12:
        tday = "PM"
        new_hour-=12
    else:
        tday="AM"
        new_hour+=12

    if days > 0:
        if days==1:   
            days_later = " (next day)"
        else:
            days_later = " (" + str(days) + " days later)"
    else:
        days_later=""

    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    if starting_day:
        weeks = days//7 + 1
        index = weekdays.index(starting_day.lower().capitalize()) + days
        if index<=6:
            new_day = " "+weekdays[index]
        else:
            new_day = " "+weekdays[index-7*weeks]     
    else:
        new_day = ""
    new_time = str(new_hour) + ":" + ('0' + str(new_mint) if new_mint < 10 else str(new_mint)) + " " + tday + ("," if new_day else "") + new_day + days_later


    return new_time


print(add_time('2:59 AM', '24:00', 'saturDay'))