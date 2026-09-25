# Electrical Power Calculator

print("===== Electrical Power Calculator =====")
print("1. DC Power")
print("2. AC Power")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))

    power = voltage * current

    print("\nElectrical Power =", round(power, 2), "W")

elif choice == 2:
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))
    power_factor = float(input("Enter power factor (0 to 1): "))

    power = voltage * current * power_factor

    print("\nAC Electrical Power =", round(power, 2), "W")

else:
    print("Invalid choice!")