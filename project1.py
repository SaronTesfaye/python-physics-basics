initial = float(input("Enter the number of initial position: "))
velocity = float(input("Enter the number of velocity: "))
time = float(input("Enter the time: "))
# x = xo + vt
x = initial + velocity * time
if x > 0:
    print("the position of an object is in the right side")
elif x == 0:
    print("the position of an object is in the origin ")
else:
    print("the position of an object is in the left side")
print(f"the position of an object is {x}meter in {time}second/s")