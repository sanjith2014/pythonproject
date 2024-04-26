light = input("Enter the traffic light colour from the given option(red,yellow,green)")
light = light.lower()
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")
else:
    print("Choose from the given option")
