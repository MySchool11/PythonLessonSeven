__author__ = "Mr Bancroft"

age = int(input("What is your age: "))
if 16 <= age <= 65:  # This is the same as "if age >= 16 and age <+ 65:" see if you can work out why?
                     # you could also change it to "if 15 < age < 66:", again think about why
    print("The chances are you work.")
if age < 16 or age > 65:  # Here we use an or operator so only one has to be true for the statement to be true
                          # whereas for the and statement both must be true for the statement to be true
    print("The chances are you do not work.")

