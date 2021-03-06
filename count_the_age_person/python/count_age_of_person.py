from datetime import datetime


def calculate_age(date_obj):
    current_date = datetime.now()
    age = current_date - date_obj
    print("Current age (days): {}".format(age.days))
    print("Current age (years): {0:.2f}".format(age.days / 365))


if __name__ == "__main__":
    age_string = input("Please insert birth year (mm/dd/yyyy): ")

    try:
        birth_date = datetime.strptime(age_string, "%m/%d/%Y")
    except:
        print("invalid date format: try mm/dd/yyyy.")
    else:
        calculate_age(birth_date)
