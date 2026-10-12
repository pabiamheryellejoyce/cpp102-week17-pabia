readings = [28, 31, 35, 37, 29]

def classify_temperature(temperature):
    if temperature < 30:
        return "NORMAL"
    elif temperature <= 35:
        return "WARNING"
    else:
        return "CRITICAL"


def view_readings(readings):
    print("\nCURRENT READINGS")
    print("------------------")

    if len(readings) == 0:
        print("No readings available.")
    else:
        for i in range(len(readings)):
            print(f"Reading {i + 1}: {readings[i]} °C")


def add_reading(readings):
    user_input = input("Enter new reading: ")

    if user_input.strip() == "":
        print("Invalid input. The reading cannot be empty.")
        return

    try:
        temperature = int(user_input)
    except ValueError:
        print("Invalid input. Enter a whole number only.")
        return

    # Reject decimals and other non-integer formats
    if user_input.strip() != str(temperature):
        print("Invalid input. Enter a whole number only.")
        return

    if temperature < 0 or temperature > 100:
        print("Invalid reading. Enter a value from 0 to 100.")
    else:
        readings.append(temperature)
        print("Reading added successfully.")


def classify_readings(readings):
    print("\nREADING CLASSIFICATION")
    print("------------------")

    if len(readings) == 0:
        print("No readings available.")
        return

    for temperature in readings:
        category = classify_temperature(temperature)
        print(f"{temperature} °C -> {category}")


def generate_summary(readings):
    if len(readings) == 0:
        print("\nNo readings available for summary.")
        return

    total = 0
    minimum = readings[0]
    maximum = readings[0]

    normal_count = 0
    warning_count = 0
    critical_count = 0

    for temperature in readings:
        # Calculate total
        total += temperature

        # Find minimum and maximum
        if temperature < minimum:
            minimum = temperature

        if temperature > maximum:
            maximum = temperature

        # Classify and count readings
        category = classify_temperature(temperature)

        if category == "NORMAL":
            normal_count += 1
        elif category == "WARNING":
            warning_count += 1
        else:
            critical_count += 1

    number = len(readings)
    average = total / number

    # Calculate category percentages
    normal_percentage = normal_count / number * 100
    warning_percentage = warning_count / number * 100
    critical_percentage = critical_count / number * 100

    # Determine overall status
    if critical_count >= 1:
        status = "ATTENTION REQUIRED"
    elif warning_count >= 1:
        status = "MONITOR"
    else:
        status = "NORMAL"

    # Display summary
    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {number}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")

    print()
    print(f"NORMAL   : {normal_count} ({normal_percentage:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_percentage:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_percentage:.2f}%)")

    print(f"\nOverall Status: {status}")


def main():
    readings = [28, 31, 35, 37, 29]

    while True:
        print("\nSIMULATED DEVICE MONITORING SYSTEM")
        print("------------------")
        print("[1] View Readings")
        print("[2] Add Reading")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            view_readings(readings)

        elif choice == "2":
            add_reading(readings)

        elif choice == "3":
            classify_readings(readings)

        elif choice == "4":
            generate_summary(readings)

        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()