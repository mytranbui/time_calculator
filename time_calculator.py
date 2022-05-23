def monday():
    return "Monday"
def tuesday():
    return "Tuesday"
def wednesday():
    return "Wednesday"
def thursday():
    return "Thursday"
def friday():
    return "Friday"
def saturday():
    return "Saturday"
def sunday():
    return "Sunday"
def default():
    return "Incorrect day"

## Only works with python3
# def match_day(day):
#     match day:
#         case "Monday":
#             return 1
#         case "Tuesday":
#             return 2
#         case "Wednesday":
#             return 3
#         case "Thursday":
#             return 4
#         case "Friday":
#             return 5
#         case "Saturday":
#             return 6
#         case "Sunday":
#             return 7
#         case _:
#             return 0

def match_day(day):
    if day == "Monday":
       return 1
    elif day == "Tuesday":
       return 2
    elif day == "Wednesday":
       return 3
    elif day == "Thursday":
       return 4
    elif day == "Friday":
       return 5
    elif day == "Saturday":
       return 6
    elif day == "Sunday":
       return 7
    else:
       return 0

weekday = {
    0: default,
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def which_day(day, add_day):
    if match_day(day) == 0:
        return "Incorrect day"
    nbr = (match_day(day) + add_day % 7) % 7
    nbr = 7 if nbr == 0 else nbr
    day = weekday[nbr]()
    return day

def add_time(start, duration, day=None):
    start_list = start.split()
    ampm = start_list[1]
    start_hr_mn = start_list[0].split(':')
    duration_hr_mn = duration.split(':')
    total_min = int(start_hr_mn[1]) + int(duration_hr_mn[1])
    add_hr = int(total_min / 60)
    total_hr = int(start_hr_mn[0]) + int(duration_hr_mn[0]) + add_hr
    chg_ampm = int(total_hr / 12) % 2
    next_day = int(total_hr / 24)
    if chg_ampm == 1 and ampm == "AM":
        ampm = "PM"
    elif chg_ampm == 1 and ampm == "PM":
        ampm = "AM"
        next_day += 1
    total_hr %= 12
    total_hr = 12 if total_hr == 0 else total_hr
    new_time = str(total_hr) + ':' + str(total_min % 60).rjust(2, '0') + ' ' + ampm
    if day != None:
        new_time += ", " + which_day(day[0].upper() + day[1:].lower(), next_day)
    if next_day == 1:
        new_time += " (next day)"
    elif next_day > 1:
        new_time += " (" + str(next_day) + " days later)"
    return new_time

def main():
    print("Result :  ",add_time("11:06 PM", "2:02"))
    print("Expected : 1:08 AM")
    print("------------------------------------")
    print("Result :  ",add_time("3:00 PM", "3:10"))
    print("Expected : 6:10 PM")
    print("------------------------------------")
    print("Result :  ",add_time("11:43 AM", "00:20"))
    print("Expected : 12:03 PM")
    print("------------------------------------")
    print("Result :  ",add_time("10:10 PM", "3:30"))
    print("Expected : 1:40 AM (next day)")
    print("------------------------------------")
    print("Result :  ",add_time("11:30 AM", "2:32", "Monday"))
    print("Expected : 2:02 PM, Monday")
    print("------------------------------------")
    print("Result :  ",add_time("6:30 PM", "205:12"))
    print("Expected : 7:42 AM (9 days later)")
    print("------------------------------------")
    print("Result :  ",add_time("11:55 AM", "3:12"))
    print("Expected : 3:07 PM")
    print("------------------------------------")
    print("Result :  ",add_time("11:43 PM", "24:20", "tueSday"))
    print("Expected : 12:03 AM, Thursday (2 days later)")
    print("------------------------------------")
    print("Result :  ",add_time("8:16 PM", "466:02", "tuesday"))
    print("Expected : 6:18 AM, Monday (20 days later)")
    print("------------------------------------")
    print("Result :  ",add_time("2:59 AM", "24:00", "saturDay"))
    print("Expected : 2:59 AM, Sunday (next day)")
    print("------------------------------------")
    print("Result :  ",add_time("11:59 PM", "24:05", "Wednesday"))
    print("Expected : 12:04 AM, Friday (2 days later)")
    print("------------------------------------")
    print("Result :  ",add_time("11:59 PM", "24:05", "ndy"))

main()
