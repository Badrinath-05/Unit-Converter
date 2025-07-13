def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def mm_to_inches(mm):
    return mm / 25.4

def kg_to_pounds(kg):
    return kg * 2.20462

def newton_to_dyne(newton):
    return newton * 100000

def pascal_to_bar(pascal):
    return pascal / 100000

def joule_to_calorie(joule):
    return joule / 4.184

def show_menu():
    print("\n🔧 Welcome to the Mechanical Unit Converter 🔧")
    print("Select the conversion you want to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. mm to inches")
    print("3. kg to pounds")
    print("4. Newton to dyne")
    print("5. Pascal to Bar")
    print("6. Joule to Calorie")
    print("7. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c} °C = {round(f, 2)} °F")

    elif choice == "2":
        mm = float(input("Enter length in mm: "))
        inches = mm_to_inches(mm)
        print(f"{mm} mm = {round(inches, 3)} inches")

    elif choice == "3":
        kg = float(input("Enter mass in kg: "))
        pounds = kg_to_pounds(kg)
        print(f"{kg} kg = {round(pounds, 3)} pounds")

    elif choice == "4":
        n = float(input("Enter force in Newton: "))
        dyne = newton_to_dyne(n)
        print(f"{n} N = {int(dyne)} dyne")

    elif choice == "5":
        p = float(input("Enter pressure in Pascal: "))
        bar = pascal_to_bar(p)
        print(f"{p} Pa = {round(bar, 5)} bar")

    elif choice == "6":
        j = float(input("Enter energy in Joules: "))
        cal = joule_to_calorie(j)
        print(f"{j} J = {round(cal, 2)} calories")

    elif choice == "7":
        print("Thanks for using the converter. Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice. Please enter a number from 1 to 7.")

    again = input("\nDo you want to convert another unit? (yes/no): ").lower()
    if again != "yes":
        print("👋 Exiting the converter. Have a great day!")
        break
