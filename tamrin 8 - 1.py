def Zarb(x, y):
    result = {}

    result["s"] = x["s"] * y["s"]
    result["m"] = x["m"] * y["m"]

    return result

def Taghsim(x, y):
    resultt = {} 

    resultt["s"] = x["s"] * y["m"]
    resultt["m"] = x["m"] * y["s"]

    return resultt

def Plus(x, y):
    rresult = {} 
    
    if x["m"] != y["m"]:
        rresult["s"] = (x["s"] * y["m"]) + (y["s"] * x["m"])
        rresult["m"] = x["m"] * y["m"]
        return rresult
    
    else:
        rresult["s"] = x["s"] + y["s"]
        rresult["m"] = x["m"]
        return rresult

def Tafrigh(x, y):
    reesult = {} 
    
    if x["m"] != y["m"]:
        reesult["s"] = (x["s"] * y["m"]) + (y["s"] * x["m"])
        reesult["m"] = x["m"] * y["m"]
        return reesult
    
    else:
        reesult["s"] = x["s"] + y["s"]
        reesult["m"] = x["m"]
        return reesult

sk1 = int(input("Enter the numerator of first fraction: ")) # صورت کسر اول
mk1 = int(input("Enter the denominator of first fraction: ")) # مخرج کسر اول

sk2 = int(input("Enter the numerator of second fraction: ")) # صورت کسر دوم
mk2 = int(input("Enter the denominator of second fraction: ")) # مخرج کسر دوم

kasr1 = {"s" : sk1, "m" : mk1}
kasr2 = {"s" : sk2, "m" : mk2}

resultZ = Zarb(kasr1 , kasr2)
print("The product is equal to", resultZ)

resultTagh = Taghsim(kasr1 , kasr2)
print("The result of division is equal to -> ", resultTagh)

resultP = Plus(kasr1 , kasr2)
print("The sum is equal to", resultP)

resultTaf = Tafrigh(kasr1 , kasr2)
print("The result of subtraction is equal to -> ", resultTaf)