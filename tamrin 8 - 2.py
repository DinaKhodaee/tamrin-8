def summTime(x, y):
    result = {}

    result["s"] = x["s"] + y["s"]
    result["m"] = x["m"] + y["m"]
    result["h"] = x["h"] + y["h"]

    if result["s"] >= 60:
        result["s"] -= 60
        result["m"] += 1

    if result["m"] >= 60:
        result["m"] -= 60
        result["h"] += 1

    return result

def subTime(x, y):
    result = {}

    if x["h"] > y["h"]:
        result["h"] = x["h"] - y["h"]
    else:
        result["h"] = y["h"] - x["h"]

    if x["m"] > y["m"]:
        result["m"] = x["m"] - y["m"]
    else:
        result["m"] = y["m"] - x["m"]
    
    if x["s"] > y["s"]:
        result["s"] = x["s"] - y["s"]
    else:
        result["s"] = y["s"] - x["s"]
    
    if result["s"] < 0:
        result["s"] += 60
        result["m"] -= 1

    if result["m"] < 0:
        result["m"] += 60
        result["h"] -= 1

    return result

def show(x):
    print(x["h"], ":", x["m"],":", x["s"])

def sec(x, y):
    t1 = (x["h"] * 3600) + (x["m"] * 60) + x["s"]
    t2 = (y["h"] * 3600) + (y["m"] * 60) + y["s"]
    t3 = t1 + t2

    th1 = t1 // 3600 
    tm1 = ((t1 % 3600) // 60)
    ts1 = t1 % 60

    th2 = t2 // 3600 
    tm2 = ((t2 % 3600) // 60)
    ts2 = t2 % 60

    return th1, tm1, ts1, th2, tm2, ts2, t3

h1 = int(input("Enter your first time by hour: "))
m1 = int(input("Enter your first time by minute: "))
s1 = int(input("Enter your first time by second: "))

print(" ")

h2 = int(input("Enter your second time by hour: "))
m2 = int(input("Enter your second time by minute: "))
s2 = int(input("Enter your second time by second: "))

print(" ")

time1 = {"h":h1, "m":m1, "s":s1}
time2 = {"h":h2, "m":m2, "s":s2}

sTime = summTime(time1, time2)
print("The sum is equal -> ", end = "")
show(sTime)

suTime = subTime (time1, time2)
print("The division is equal -> ", end = "")
show(suTime)
print(" ")

TimetoSec = sec(time1, time2)
print("Your first time to seconds ->", TimetoSec[0], ":", TimetoSec[1], ":", TimetoSec[2])
print(" ")
print("Your second time to seconds ->", TimetoSec[3], ":", TimetoSec[4], ":", TimetoSec[5])
print(" ")
print("The sum of seconds is equal to ->", TimetoSec[6])