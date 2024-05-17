print("Welcome to Uniten Sport Rental System")
print("List of Stations\n1. Futsal\n2. Sepak Takraw\n3. Basketball\n4. Badminton")


court_type = int(input("Please select the court number: "))

while court_type < 1 or court_type > 4:
    input("You inserted invalid number. Press enter to try again")
    court_type = int(input("Please select the court number: "))

if court_type == 1:
    print("You inserted number 1. Futsal")
elif court_type == 2:
    print("You inserted number 2. Sepak Takraw")
elif court_type == 3:
    print("You inserted number 3. Basketball")
elif court_type == 4:
    print("You inserted number 4. Badminton")

student = input("Are you Uniten Student? (Type Yes or No): ").lower()

while student != "yes" and student != "no":
    input("You inserted invalid answer. Press enter to try again")
    student = input("Are you Uniten Student? (Type Yes or No): ").lower()

if student == "yes":
    print("You chose Uniten Student as option")
    student = True
else:
    print("You chose not Uniten Student as option")
    student = False

day = input("When would you like to book the court, mention the day only: ").capitalize()

weekdays = ["Monday", "Tuesday", "Wednesday", "Friday", "Thursday"]
weekend = ["Saturday", "Sunday"]

while day not in weekdays and day not in weekend:
    input("You inserted wrong day. Press enter to try again.")
    day = input("When would you like to book the court, mention the day only: ").capitalize()

print("You chose", day, "as option.")


def int_input(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return user_input
        
hours = int_input("How many hours would you like to book/rent the court (Kindly type numbers only):")
        
def price_calc():
    if court_type == 1:
        if student:
            price = 50
        else:
            if day in weekdays:
                price = 60
            else:
                price = 80

    elif court_type == 2:
        if student:
            if day in weekdays:
                price = 20
            else:
                price = 25
        else:
            if day in weekdays:
                price = 60
            else:
                price = 65

    elif court_type == 3:
        if student:
            price = 55
        else:
            if day in weekdays:
                price = 65
            else:
                price = 85

    elif court_type == 4:
        if student:
            if day in weekdays:
                price = 30
            else:
                price = 60
        else:
            if day in weekdays:
                price = 60
            else:
                price = 65

    else:
        print("error")

    return price


def total_calc():
    amount = price_calc()*hours
    return amount

print("Rental details")
print("Court: ", court_type)
print("Uniten Student: ", student)
print("Day: ", day)
print("Hours: ", hours)
print("total amount:", total_calc())

ringgit = [1, 5, 10, 20, 50, 100]


total_paid = 0

while total_calc() > total_paid:
    pay = int(input("Insert payment: "))
    while pay not in ringgit:
        print("Please insert rm 1, 5, 10, 20, 50 100 only")
        pay = int(input("Insert payment: "))
    total_paid += pay
    balance = total_calc() - pay
    print("balance: ", balance)

if total_calc() == total_paid:
    print("thanks")
elif total_calc() < total_paid:
    balance = total_paid - total_calc()
    print("baki amik kat mesin : rm", balance)
else:
    print("error")
        



