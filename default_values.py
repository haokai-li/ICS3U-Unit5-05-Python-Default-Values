#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about address


def word_upper(
    full_name,
    street_number,
    street_type,
    city,
    province,
    postal_code,
    apartment_number=None,
):
    # This function is about address

    final_address = None

    # process
    full_name_upper = full_name.upper()
    street_type_upper = street_type.upper()
    city_upper = city.upper()
    province_upper = province.upper()
    postal_code_upper = postal_code.upper()

    if apartment_number is not None:
        final_address = (
            full_name_upper
            + "\n"
            + str(apartment_number)
            + "-"
            + str(street_number)
            + " "
            + street_type_upper
            + "\n"
            + city_upper
            + " "
            + province_upper
            + "  "
            + postal_code_upper
        )
    else:
        final_address = (
            full_name_upper
            + "\n"
            + str(street_number)
            + " "
            + street_type_upper
            + "\n"
            + city_upper
            + " "
            + province_upper
            + "  "
            + postal_code_upper
        )

    return final_address


def main():
    # This function just call other functions
    user_apartment_string = None

    print("This Program formats your address to a mailing address.")
    print("")

    # input
    user_full_name_string = input("Enter your full name: ")
    user_if_apartment_string = input("Do you live in a apartment? (y/n): ")
    if (
        user_if_apartment_string.upper() == "Y"
        or user_if_apartment_string.upper() == "YES"
    ):
        user_apartment_string = input("Enter your apartment number: ")
    user_street_string = input("Enter your street number: ")
    user_street_type_string = input(
        "Enter your street name AND type (Main St, Express Pkwy...): "
    )
    user_city_string = input("Enter your city: ")
    user_province_string = input(
        "Enter your province (as an abbreviation, ex: ON, BC..): "
    )
    user_postal_code_string = input("Enter your postal code (123 456): ")
    print("")

    try:
        if (
            user_if_apartment_string.upper() == "Y"
            or user_if_apartment_string.upper() == "YES"
        ):
            user_apartment_number = int(user_apartment_string)
        user_street_number = int(user_street_string)

        # call functions
        if user_apartment_string is not None:
            final_upper = word_upper(
                full_name=user_full_name_string,
                street_number=user_street_number,
                street_type=user_street_type_string,
                city=user_city_string,
                province=user_province_string,
                postal_code=user_postal_code_string,
                apartment_number=user_apartment_number,
            )
        else:
            final_upper = word_upper(
                full_name=user_full_name_string,
                street_number=user_street_number,
                street_type=user_street_type_string,
                city=user_city_string,
                province=user_province_string,
                postal_code=user_postal_code_string,
            )

        # output
        print(final_upper)

    except Exception:
        # output
        print("You have an error input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
