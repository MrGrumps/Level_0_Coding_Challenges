#Task 0.8
def conv_time(x):
    hour = x // 60
    minutes = x % 60
    print(str(hour) + " hours, " + str(minutes) + " minutes")

conv_time(133)