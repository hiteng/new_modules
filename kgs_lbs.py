
weight = input("Enter your weight: ")
opt = input("k or l: ")
if opt == "l":
    print("Weight in kgs:" + str(float(weight) * 0.453))
elif opt == "k":
    print("Weight in lbs:" + str(float(weight) * 2.204))
