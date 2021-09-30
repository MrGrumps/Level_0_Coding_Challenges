#Task 0.8
def conv_time(x):
    hour = x // 60
    minutes = x % 60
    if hour == 0 and minutes < 2:
        print(str(minutes) + " minute")
    elif hour == 0 and minutes > 1:
        print(str(minutes) + " minutes")
    elif hour < 2 and minutes == 0:
        print(str(hour) + " hour")
    elif hour > 1 and minutes == 0:
        print(str(hour) + " hours")
    elif hour == 1 and minutes < 2:
        print(str(hour) + " hour, " + str(minutes) + " minute")
    elif hour == 1 and minutes > 1:
        print(str(hour) + " hour, " + str(minutes) + " minutes")
    elif hour > 1 and minutes < 2:
        print(str(hour) + " hours, " + str(minutes) + " minute")
    else:
        print(str(hour) + " hours, " + str(minutes) + " minutes")

conv_time(61)