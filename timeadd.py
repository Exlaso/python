def add_time(start, duration):

    hour, minute = start.split(':')
    min, time_zone = minute.split()
    end_date, end_minute = duration.split(':')

    if time_zone.upper() == 'AM':
        d = 24
        timez = 'AM'

    else: 
        d = 12
        timez = 'PM'
    if (int(min)+int(end_minute)) > 60:
        sumofmin = (int(min)+int(end_minute)) % 60
        hour = int(hour) + ((int(min)+int(end_minute)) / 60)
    else:
        sumofmin = (int(min)+int(end_minute))
    if (int(hour)+int(end_date)) > d:
        sumofhour = ((int(hour)+int(end_date)) % d)
        days = ((int(hour)+int(end_date)) / 24)

    else:
        sumofhour = ((int(hour)+int(end_date)))
        days = 0
    if sumofhour >= 12: 
        if sumofhour == 12 and sumofmin >= 0:
            sumofhour = 12
            timez = "PM"    
        else:    
            sumofhour %= 12
            timez = "AM"    
    ret0 = (str(sumofhour)+':'+str(sumofmin).zfill(2),timez,str(round(days))+" days later")
    ret = ret0[0]+" "+ret0[1]+" "
    if days > 0:
        ret += ret0[2]     
    return ret

print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))