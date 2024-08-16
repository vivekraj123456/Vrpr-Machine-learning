import re
from info import info


def validate(plate_number):
    pattern = r"^[A-Za-z]{2}[ -]?[0-9]{2}[ -]?[A-Za-z]{1,2}[ -]?[0-9]{4}$"
    match = re.match(pattern, plate_number)
    if match:
        print("Valid plate number:", plate_number)
        # reg_info = info(plate_number, api_key=api_key)
        # print(reg_info)

        return True

    else:
        print("Invalid plate number:", plate_number)
