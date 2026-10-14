from datetime import datetime

name = "Zi"
Surname = "Liu"
Brithday = 13

today = datetime.today().strftime('%m')
print(today)
todayint = int(today)

if todayint == 1:
    print("Janary")
elif todayint == 2:
    print("February")
elif todayint == 3:
    print("March")
elif todayint == 4:
    print("April")
elif todayint == 5:
    print("May")
elif todayint == 6:
    print("June")
elif todayint == 7:
    print("July")
elif todayint == 8:
    print("August")
elif todayint == 9:
    print("September")
elif todayint == 10:
    print("October")
elif todayint == 11:
    print("November")
elif todayint == 12:
    print("December")
else:
    print("uuuuuuuu")