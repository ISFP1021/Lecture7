def isnumberdivisiblebythree (n):
    if n%3==0:
        return True
    return False
num=int(input(print("Give me a number")))
if isnumberdivisiblebythree (num):
    print("%d is divisible by 3" %num)
else:
    print("%d is not divisible by 3" % num)